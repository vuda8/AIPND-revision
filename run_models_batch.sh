#!/bin/bash

# PROGRAMMER: Do Anh Vu
# DATE CREATED: 2024-05-20
# REVISED DATE: [Revised Date]
# PURPOSE: Runs all three models to classify the uploaded images.
#          The results from each model architecture are stored in separate files.
#
# Usage: sh run_models_batch_uploaded.sh

python check_images.py --dir uploaded_images/ --arch resnet > resnet_uploaded-images.txt
python check_images.py --dir uploaded_images/ --arch alexnet > alexnet_uploaded-images.txt
python check_images.py --dir uploaded_images/ --arch vgg > vgg_uploaded-images.txt
