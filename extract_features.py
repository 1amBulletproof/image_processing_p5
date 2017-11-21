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
def extract_features(src_image_bgr, src_image_gray):
    feature_vector = []
    src_image_hsv = cv2.cvtColor(src_image_bgr, cv2.COLOR_BGR2HSV)

    #Image size/shape
    feature_vector.append(src_image_bgr.shape[0])#height
    feature_vector.append(src_image_bgr.shape[1])#width

    # gray-scale histogram descriptors
    append_gray_histogram_descriptors(src_image_gray, feature_vector)

    # color histogram descriptors
    append_color_histogram_descriptors(src_image_bgr, feature_vector)

    #Edge Detection/Contour

    #Fourier descriptors

    #Thumbnail image

    #corner descriptors

    #Necronomicon descriptors

    #shape descriptors

    #SIFT descriptors
    append_sift_descriptors(src_image_gray, feature_vector)

    # do SURF stuff

    #print("feature_vector is " + str(len(feature_vector)) + " long")
    return feature_vector


def append_sift_descriptors(src_image_gray, feature_vector):
    #TODO: create a normalized histogram of the SIFT stuff then call append_histogram_descriptors?
    # SIFT: returns 2d descriptor array: capture as stats or histogram or use all values
    sift = cv2.xfeatures2d.SIFT_create(1)
    (keypoints, descriptors) = sift.detectAndCompute(src_image_gray, None)
    #Just write them all to string...
    #feature_vector.extend(descriptors[0])
    sift_std = numpy.std(descriptors)
    sift_mean = numpy.mean(descriptors)
    sift_median = numpy.median(descriptors)
    sift_max = numpy.amax(descriptors)
    sift_variance = numpy.var(descriptors)
    feature_vector.append(sift_std)
    feature_vector.append(sift_mean)
    feature_vector.append(sift_median)
    feature_vector.append(sift_max)
    feature_vector.append(sift_variance)
    return


def append_gray_histogram_descriptors(src_image_gray, feature_vector):
    #get histogram
    gray_histogram = cv2.calcHist([src_image_gray], [0], None, [256],[0,256])
    #cv2.normalize(gray_histogram, gray_histogram)
    gray_histogram = gray_histogram.flatten()

    append_histogram_descriptors(gray_histogram, feature_vector)
    return


def append_color_histogram_descriptors(src_image_bgr, feature_vector):
    # get B, G, R histograms
    channels = cv2.split(src_image_bgr)
    for channel in channels:
        histogram = cv2.calcHist([channel], [0], None, [256], [0,256])
        #cv2.normalize(histogram, histogram)
        histogram = histogram.flatten()
        append_histogram_descriptors(histogram, feature_vector)
    return


def append_histogram_descriptors(histogram, feature_vector):
    #extract descriptors: mean, std_dev, max val & index of max val (color value)
    mean, std_dev = cv2.meanStdDev(histogram)
    max_val = numpy.amax(histogram)
    max_index = numpy.argmax(histogram)

    feature_vector.append(mean[0][0])
    feature_vector.append(std_dev[0][0])
    feature_vector.append(max_val)
    feature_vector.append(max_index)
    return


##Load Image
if __name__=='__main__':
    filename = ''

    # Load the source image.
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        orig_src_image_bgr = cv2.imread(filename, 1) # load as color
        orig_src_image_gray = cv2.imread(filename, 0) # load as gray
    else:
        print "ERROR: %s image.png" % (sys.argv[0])
        sys.exit(1)

    #Extract image features
    feature_vector = extract_features(orig_src_image_bgr, orig_src_image_gray)

    #Print features
    print "%s,%s" % (filename, ','.join(str(x) for x in feature_vector))
