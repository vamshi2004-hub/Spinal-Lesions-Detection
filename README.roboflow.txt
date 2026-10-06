
Backspine - v3 2024-08-23 9:07am
==============================

This dataset was exported via roboflow.com on December 4, 2024 at 2:16 PM GMT

Roboflow is an end-to-end computer vision platform that helps you
* collaborate with your team on computer vision projects
* collect & organize images
* understand and search unstructured image data
* annotate, and create datasets
* export, train, and deploy computer vision models
* use active learning to improve your dataset over time

For state of the art Computer Vision training notebooks you can use with this dataset,
visit https://github.com/roboflow/notebooks

To find over 100k other datasets and pre-trained models, visit https://universe.roboflow.com

The dataset includes 2464 images.
L1-S1 are annotated in Multi-Class Classification format.

The following pre-processing was applied to each image:
* Auto-orientation of pixel data (with EXIF-orientation stripping)
* Resize to 512x512 (Stretch)

The following augmentation was applied to create 3 versions of each source image:
* 50% probability of horizontal flip
* Equal probability of one of the following 90-degree rotations: none, clockwise, counter-clockwise, upside-down
* Random rotation of between -23 and +23 degrees
* Random shear of between -15° to +15° horizontally and -15° to +15° vertically
* Salt and pepper noise was applied to 5 percent of pixels

The following transformations were applied to the bounding boxes of each image:
* Randomly crop between 0 and 20 percent of the bounding box


