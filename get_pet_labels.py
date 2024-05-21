#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Do Anh Vu
# DATE CREATED: 2024-05-20                            
# REVISED DATE: 
# PURPOSE: Create a function that creates pet image labels by creating a dictionary
#          with key=filename and value=file label.
#          The labels are formatted with lower case letters and single space separating each word.

# Importing necessary modules
from os import listdir

def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains the following item:
         index 0 = pet image label (string)
    """
    # Retrieve the filenames from folder image_dir
    filename_list = listdir(image_dir)
    
    # Creates empty dictionary named results_dic
    results_dic = dict()
    
    # Processes through each file in the directory, extracting only the words
    # of the filename and converting them to lowercase, then storing as a list
    for filename in filename_list:
        if filename.startswith('.'):
            continue
        
        # Skipping file if starts with . (like .DS_Store of Mac OSX) because it 
        # isn't an image file
        if filename[0] != ".":
            # Sets pet_image variable to a filename 
            pet_image = filename
            
            # Sets string to lower case letters
            low_pet_image = pet_image.lower()
            
            # Splits lower case string by _ to break into words 
            word_list_pet_image = low_pet_image.split("_")
            
            # Creates pet_name starting as empty string
            pet_name = ""
            
            # Loops to check if word in pet name is only alphabetic characters
            for word in word_list_pet_image:
                if word.isalpha():
                    pet_name += word + " "
                    
            # Strip off starting/trailing whitespace characters 
            pet_name = pet_name.strip()
            
            # If filename doesn't already exist in dictionary add it with the 
            # value as a list containing pet_name
            if filename not in results_dic:
                results_dic[filename] = [pet_name]
            else:
                print(f"** Warning: Duplicate files exist in directory: {filename}")
                
    # Return results dictionary
    return results_dic

