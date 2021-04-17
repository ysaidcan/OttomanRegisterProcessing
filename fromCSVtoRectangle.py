#!/usr/bin/env python

import os
from glob import glob

from imageio import imread, imsave
from tqdm import tqdm
import ntpath
import numpy as np
import cv2
import pandas as pd

from dh_segment.io import PAGE
from dh_segment.inference import LoadedModel
from dh_segment.post_processing import boxes_detection, binarization

# To output results in PAGE XML format (http://www.primaresearch.org/schema/PAGE/gts/pagecontent/2013-07-15/)


if __name__ == '__main__':

    # If the model has been trained load the model, otherwise use the given model

    input_files = glob('NFS_2865_Manisa/*')
    output_dir = 'processed_images_model_mixed_17_04_2021'


    # PAGE XML format output




    iznik_individuals = pd.read_csv( 'numbers_individuals_combined_alternative.csv');

    for filename in tqdm(input_files, desc='Processed files'):
            # For each image, predict each pixel's label


            # Draw page box on original image and export it. Add also box coordinates to the txt file
        original_img = imread(filename, pilmode='RGB')
        if True:
                # Write corners points into a .txt file
            filename_w_o_ext = os.path.splitext(filename)[0]
            filename = ntpath.basename(filename_w_o_ext)
            data = filename.split("_")
            registerID = float(data[4])
            pageNum = float(data[5])
            american = iznik_individuals['NumregisterID'] == registerID


                # Create variable with TRUE if age is greater than 50
            elderly = iznik_individuals['NumPageNum'] == pageNum

            filtered=iznik_individuals[american & elderly];

            for x in range(0, len(filtered)):
                num1 = filtered['NumcoordW0'].iloc[x]
                num2 = filtered['NumcoordH0'].iloc[x]
                num3 = filtered['NumcoordW1'].iloc[x]
                num4 = filtered['NumcoordH1'].iloc[x]
                num5 = filtered['NumcoordW2'].iloc[x]
                num6 = filtered['NumcoordH2'].iloc[x]
                num7 = filtered['NumcoordW3'].iloc[x]
                num8 = filtered['NumcoordH3'].iloc[x]

                ind1 = filtered['coordW0'].iloc[x]
                ind2 = filtered['coordH0'].iloc[x]
                ind3 = filtered['coordW1'].iloc[x]
                ind4 = filtered['coordH1'].iloc[x]
                ind5 = filtered['coordW2'].iloc[x]
                ind6 = filtered['coordH2'].iloc[x]
                ind7 = filtered['coordW3'].iloc[x]
                ind8 = filtered['coordH3'].iloc[x]

                Numarray = np.array([[num1, num2], [num3, num4],[num5, num6], [num7, num8]])

                Indarray = np.array([[ind1, ind2], [ind3, ind4], [ind5, ind6], [ind7, ind8]])

                cv2.polylines(original_img, np.int32([Numarray]), True, (255, 0, 0),
                                      thickness=4)

                cv2.polylines(original_img, np.int32([Indarray]), True, (0, 255, 0),
                                  thickness=7)

                # for x in range(0, len(pred_page_coords0)):
                #    txt_coordinates += '{};{}\n'.format(filename + ",0,", format_quad_to_string(pred_page_coords0[x]))

                # Create page region and XML file


        basename = os.path.basename(filename).split('.')[0]
        imsave(os.path.join(output_dir, '{}_boxes.jpg'.format(basename)), original_img)