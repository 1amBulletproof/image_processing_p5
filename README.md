# image_processing_p5
- Description: Image Classification in OpenCV using Python
- Author: Brandon Tarney
- Date: 11/18/2017

## Details
- How-to run:
    - python2 extract_features.py IMAGE.jpg
        - outputs image features
    - extract_features.bash CSV_FILE.csv
        - outputs all image features (for any images in your current directory) to CSV_FILE
        - Be careful not to append-to an existing CSV file...must create a new one each time
    - python2 match_images.py CSV_FILE.csv
        - find the 12 closest match images (uses euclidean distance between feature vectors)

