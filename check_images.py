#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/check_images.py

# PROGRAMMER: Do Anh Vu
# DATE CREATED: 2024-05-20
# REVISED DATE: 
# PURPOSE: Classifies pet images using a pretrained CNN model, compares these
#          classifications to the true identity of the pets in the images, and
#          summarizes how well the CNN performed on the image classification task. 
#          Note that the true identity of the pet (or object) in the image is 
#          indicated by the filename of the image. Therefore, your program must
#          first extract the pet image label from the filename before
#          classifying the images using the pretrained CNN model. With this 
#          program we will be comparing the performance of 3 different CNN model
#          architectures to determine which provides the 'best' classification.
#
# Use argparse Expected Call with <> indicating expected user input:
#      python check_images.py --dir <directory with images> --arch <model>
#             --dogfile <file that contains dognames>
#   Example call:
#    python check_images_solution.py --dir pet_images/ --arch vgg --dogfile dognames.txt
##
import argparse
# Imports python modules
from time import time, sleep

# Imports print functions that check the lab
from print_functions_for_lab_checks import check_command_line_arguments, check_creating_pet_image_labels, check_classifying_images, check_classifying_labels_as_dogs, check_calculating_results

# Imports functions created for this program
from get_input_args import get_input_args
from get_pet_labels import get_pet_labels
from classifier import classifier
from classify_images import classify_images
from adjust_results4_isadog import adjust_results4_isadog
from calculates_results_stats import calculates_results_stats
from print_results import print_results

# Main program function defined below
def main():
    # Measures total program runtime by collecting start time
    start_time = time()
    
    # Parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir', type=str, default='pet_images/', help='path to the folder of pet images')
    parser.add_argument('--arch', type=str, default='vgg', help='CNN model architecture to use for classification')
    parser.add_argument('--dogfile', type=str, default='dognames.txt', help='text file with dog names')
    
    args = parser.parse_args()
    
    # Check command line arguments using args  
    check_command_line_arguments(args)

    # Create pet image labels
    results = get_pet_labels(args.dir)
    # Check Pet Images in the results Dictionary
    check_creating_pet_image_labels(results)

    # Classify images and compare labels
    classify_images(args.dir, results, args.arch)
    # Check Results Dictionary
    check_classifying_images(results)    

    # Adjust results to determine if classifier correctly classifies 'a dog' or 'not a dog'
    adjust_results4_isadog(results, args.dogfile)
    # Check Results Dictionary for is-a-dog adjustment
    check_classifying_labels_as_dogs(results)

    # Calculate results statistics
    results_stats = calculates_results_stats(results)
    # Check Results Statistics Dictionary
    check_calculating_results(results, results_stats)

    # Print results
    print_results(results, results_stats, args.arch, True, True)
    
    # Measure total program runtime by collecting end time
    end_time = time()
    # Computes overall runtime in seconds & prints it in hh:mm:ss format
    tot_time = end_time - start_time
    print("\n** Total Elapsed Runtime:",
          str(int((tot_time / 3600))) + ":" + str(int((tot_time % 3600) / 60)) + ":" + str(int((tot_time % 3600) % 60)))
    

# Call to main function to run the program
if __name__ == "__main__":
    main()
