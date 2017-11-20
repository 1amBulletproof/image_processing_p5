#!/usr/bin/env python
#@author: Brandon Tarney
#@Date: 11/19/2017

## WHAT: Sample program to extract image features
## HOW: python extract_features.py image_100.jpg

import cv2
import sys
import random
import numpy

#Extracts features from image and returns them as a vector
def extract_features(src_image):
    feature_vector = []

    #Image size/shape
    feature_vector.append(src_image.shape[0])#height
    feature_vector.append(src_image.shape[1])#width

    # gray-scale histogram descriptors
    #append_histogram_descriptors(src_image, feature_vector)

    # color histogram descriptors
    #append_histogram_descriptors(src_image, feature_vector)

    #Edge Detection/Contour

    #Fourier descriptors

    #Thumbnail image

    #corner descriptors

    #Necronomicon descriptors

    #shape descriptors

    # SIFT: returns 2d descriptor array, so take avg of each, or just write them out linearly...or take average of the first value etc.. 
    sift = cv2.xfeatures2d.SIFT_create(1)
    (keypoints, descriptors) = sift.detectAndCompute(src_image, None)
    #Just write them all to string...
    feature_vector.extend(descriptors[0])
    '''
    # use the first 25 descriptors...
    for descriptor_vector in descriptors:
        descriptor_vector_average = numpy.mean(descriptor_vector)
        feature_vector.append(descriptor_vector_average)
    ''' 

    # do SURF stuff

    #print("feature_vector is " + str(len(feature_vector)) + " long")
    return feature_vector


def append_histogram_descriptors(src_image, feature_vector):
    #hsv_image = cv2. 
    return


##Load Image
if __name__=='__main__':
    filename = ''

    # Load the source image.
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        #orig_src_image = cv2.imread(filename, 1) # load as color
        orig_src_image = cv2.imread(filename, 0) # load as gray
    else:
        print "ERROR: %s image.png" % (sys.argv[0])
        sys.exit(1)

    #Extract image features
    feature_vector = extract_features(orig_src_image)

    #Print features
    print "%s,%s" % (filename, ','.join(str(x) for x in feature_vector))
