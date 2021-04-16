#!/usr/bin/env python

import os
from glob import glob
import ntpath
import cv2
import numpy as np
import tensorflow as tf
from imageio import imread, imsave
from tqdm import tqdm
import matplotlib.pyplot as plt

from dh_segment.io import PAGE
from dh_segment.inference import LoadedModel
from dh_segment.post_processing import boxes_detection, binarization

# To output results in PAGE XML format (http://www.primaresearch.org/schema/PAGE/gts/pagecontent/2013-07-15/)
PAGE_XML_DIR = './page_xml'

def Average(lst):
    return sum(lst) / len(lst)


def page_make_binary_mask(probs: np.ndarray, threshold: float=-1) -> np.ndarray:
    """
    Computes the binary mask of the detected Page from the probabilities outputed by network
    :param probs: array with values in range [0, 1]
    :param threshold: threshold between [0 and 1], if negative Otsu's adaptive threshold will be used
    :return: binary mask
    """

    mask = binarization.thresholding(probs, threshold)
    mask = binarization.cleaning_binary(mask, kernel_size=5)
    return mask


def format_quad_to_string(quad):
    """
    Formats the corner points into a string.
    :param quad: coordinates of the quadrilateral
    :return:
    """
    s = ''
    for corner in quad:
        s += '{},{},'.format(corner[0], corner[1])
    return s[:-1]


if __name__ == '__main__':

    # If the model has been trained load the model, otherwise use the given model
    model_dir = 'yekta\\yekta\\model_iznik_unet_all_100\\export'
    if not os.path.exists(model_dir):
        model_dir = 'demo/model/'

    input_files = glob('İznik\\train\\images\\*')

    output_dir = 'demo/processed_iznik_images_people'
    os.makedirs(output_dir, exist_ok=True)
    # PAGE XML format output
    output_pagexml_dir = os.path.join(output_dir, PAGE_XML_DIR)
    os.makedirs(output_pagexml_dir, exist_ok=True)

    # Store coordinates of page in a .txt file
    # Store coordinates of page in a .txt file
    txt_coordinates = ''
    txt_coordinates += "registerID,PageNum,objType,avgW,avgH,isLeft,isEdge,coordW0,coordH0,coordW1,coordH1,coordW2,coordH2,coordW3,coordH3\n"

    with tf.Session():  # Start a tensorflow session
        # Load the model
        m = LoadedModel(model_dir, predict_mode='filename')

        for filename in tqdm(input_files, desc='Processed files'):
            # For each image, predict each pixel's label
            prediction_outputs = m.predict(filename)
            probs = prediction_outputs['probs'][0]
            original_shape = prediction_outputs['original_shape']
            probs = probs[:, :, 2]  # Take only class '1' (class 0 is the background, class 1 is the page)
            probs = probs / np.max(probs)  # Normalize to be in [0, 1]

            # Binarize the predictions
            page_bin = page_make_binary_mask(probs)

            # Upscale to have full resolution image (cv2 uses (w,h) and not (h,w) for giving shapes)
            bin_upscaled = cv2.resize(page_bin.astype(np.uint8, copy=False),
                                      tuple(original_shape[::-1]), interpolation=cv2.INTER_NEAREST)

            plt.imshow(bin_upscaled)
            plt.show()

            # Find quadrilateral enclosing the page
            pred_page_coords = boxes_detection.find_boxes(bin_upscaled.astype(np.uint8, copy=False),
                                                          mode='min_rectangle')

            weight=bin_upscaled.shape[1]/2
            filename_w_o_ext = os.path.splitext(filename)[0]
            filename1 = ntpath.basename(filename_w_o_ext)
            data = filename1.split("_")
            registerID = data[4]
            pageNum = data[5]
            isLeft = 0
            isEdge = 0
            previousAverage = [0, 0]
            # Draw page box on original image and export it. Add also box coordinates to the txt file
            original_img = imread(filename, pilmode='RGB')
            if pred_page_coords is not None:
                for x in range(0, len(pred_page_coords)):
                    pred_page_coords_element = pred_page_coords[x]
                    cv2.polylines(original_img, [pred_page_coords_element[:, None, :]], True, (0, 255, 0), thickness=5)
                    # Write corners points into a .txt file
                    pred_page_coords_element = pred_page_coords[x]
                    typeCoord = pred_page_coords[x]
                    typeCoord_w = pred_page_coords[x][0]
                    typeCoord_h = pred_page_coords[x][1]
                    typeCoord_h1 = pred_page_coords[x][2]
                    typeCoord_h2 = pred_page_coords[x][3]
                    average = Average(typeCoord)
                    if (average[0] < weight):
                        isLeft = 1
                    max_w = max(typeCoord_w[0], typeCoord_h[0], typeCoord_h1[0], typeCoord_h2[0])
                    max_h = max(typeCoord_w[1], typeCoord_h[1], typeCoord_h1[1], typeCoord_h2[1])
                    txt_coordinates += '{},{}\n'.format(registerID + "," + pageNum + ",1," + str(int(average[0])) + "," + str(int(average[1])) + "," + str(isLeft) + "," + str(isEdge),format_quad_to_string(pred_page_coords[x]))

                    # Create page region and XML file
                    page_border = PAGE.Border(coords=PAGE.Point.cv2_to_point_list(pred_page_coords_element[:, None, :]))
            else:
                print('No box found in {}'.format(filename))
                page_border = PAGE.Border()

            basename = os.path.basename(filename).split('.')[0]
            imsave(os.path.join(output_dir, '{}_boxes.jpg'.format(basename)), original_img)

            page_xml = PAGE.Page(image_filename=filename, image_width=original_shape[1], image_height=original_shape[0],
                                 page_border=page_border)
            xml_filename = os.path.join(output_pagexml_dir, '{}.xml'.format(basename))
            page_xml.write_to_file(xml_filename, creator_name='PageExtractor')

    # Save txt file
    with open(os.path.join(output_dir, 'last_coordinates.csv'), 'w') as f:
        f.write(txt_coordinates)