NOTE: Images are in the Screenshots dropbox dir

# Written Problems HW 5
    - Author: Brandon Tarney
    - Date: 11/19/2017

## Problems

1. Histogram analysis is one of the most widely used methods to extract statistical information of an image. List and explain five statistical features that can be obtained from a histogram. Provid ehte formulation of each of those statistical features.

    - Mean or the average color value. 

    - Variance attempts to represent how diverse the pixel values are and how much they differ from the mean. This is effectively the square of the standar deviation.

    - Absolute Deviation like the variance except it represents the actual average value of variance of any given pixel from the mean, instead of 

    - Standard Deviation represents how divers the pixel values are and how much they differ from the mean. This is effectively the square root of the variance.

    - Skewness represents how much the histogram 'skews' to one side or the other. 

    - Kurtosis represents how spread-out vs. concentrated pixel values are (visually it measure the relative amount of peaks in a histogram graph). 

    - Hstogram analysis is simple to compute and intuitive. Unfortunately it does not include spatial information and is sensitive to noise.

2. List and explain three methods that can be used to capture color properties of an image.

    - Color moments or CM are simple and effective ways to determine image features. They consist of the mean, standard deviation and skewness. The formula for calculating each color moment is listed below (respectively). The benefits of using color moments are they are compact and robust, but they typically do not include enough information to describe all colors nor is there spatial information. 
    

    - Color coherence or CCV ..... Although color coherence includes spatial informaiton, it has a high computation cost. 

    - Color correlogram ....... Like color coherence, correlograms include spatial information but have an even higher computational cost, and are sensitive to noise, rotation, an scale.

    - Dominant color descriptor or DCD ... Although there is no spatial information encapsulated in the dominant color descriptor, it is one of the best descriptors since it is compact, robust, and perceptually meaningful. 

    - color structure  or CSD ...CSD does include spatial information but is sensitive ot noise,  rotation and scale (like correlogram).

    - Scalable color descriptor or SCD ....... The SCD scales to large images well meanign it's computation and compactness are execllent, but it's sensitive to noise, rotation, and scale not to mention there is no spatial information. 

3. List and explain three methods that can be used to capture shape properties of an image.
    - Shape features: 
        

While color is generally a per-pixel property, shape is measure by groups of pixels.
Shape feature extraction typically falls into one of two types:

    - Contour based feature extraction is more or less what it sounds like: finding contours or continous edges within an image. One example of contour based feature extration is the use of chain codes which are effectively N number of decision points at which point you can go in X number of directions in order to form the outline of a shape, i.e. if you can go north, south, east, or west encoded as 0,1,2,3, the chain code for a square (starting in the upper left corner) would be 2130. Simple descriptors can be used for boundaries as well, such as the length of a boundary or the curvature of a boundary or even shape number which is calculated using the smallest difference between its block chain and preset shape number block chains. 

    - Region based feature extraction extract features for the entireity of a shape, not just its boundary or contour like above. Simple regional descriptors include the area of the region (the number of pixels) the permiter of a region , the compactness of a region (calculated by comparing the permiter and area), the mean/median/min/max gray-level values for a given region and even number of pixels above/abelow a gray-value threshold in a given region. Specific algorithms such as the circularity ratio may be used as well (circularity is essentially the ratio of the area of a shape to the area of a circle having hte same perimeter, this same calculation can be made with rectangles to find the rectangularity shape feature).

    - Also there is corner detection?

It is generally believed that human visual systems use texture for recognition and interpretation so it makes sense that computers do as well. Texture variance include direcitonal vs. non-directional, smooth vs. rough, coarse vs. fine, and regulard vs. irregular. 
        - Spatial texture features are found through statistics or local pixel strcutures in the original image domain. Spatial features are meaningful and easy to understand and can be extracted from any shape without losing information but they are sensitive to noise and distortions (a common problem with any feature extraction: see several above color methods). 

    - Spectral texture are found in the fequency domain by applying a FFT to the originanl image and calculating the features from the resulting image. Spectral image features are easy to extract quickly and are excellent at uniquely identifying an image, however they have no meaning to a human and require swuare image regions with sufficient size.

