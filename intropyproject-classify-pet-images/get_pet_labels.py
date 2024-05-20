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
    Create pet image labels by creating a dictionary with key=filename and value=file label.
    The labels are formatted with lower case letters and single space separating each word.

    Parameters:
     - image_dir: Directory containing the pet images.

    Returns:
     - results_dic: Dictionary with pet image filenames as keys and their corresponding labels as values.
    """
    # Creating an empty dictionary to store results
    results_dic = {}

    # Retrieving the filenames from the specified directory
    filename_list = listdir(image_dir)

    # Iterating through the filenames to create labels
    for filename in filename_list:
        # Skipping hidden files (starting with '.')
        if filename[0] != ".":
            # Splitting the filename into words based on underscores
            word_list_pet_image = filename.lower().split("_")

            # Creating an empty string to store the label
            pet_name = ""

            # Looping through the words in the filename
            for word in word_list_pet_image:
                # Appending only alphabetic words to the label
                if word.isalpha():
                    pet_name += word + " "

            # Stripping leading/trailing whitespace characters
            pet_name = pet_name.strip()

            # Adding the filename and label to the results dictionary
            if filename not in results_dic:
                results_dic[filename] = pet_name

    return results_dic

# Example usage for testing
# if __name__ == "__main__":
#     pet_labels_dict = get_pet_labels("pet_images/")
#     print(pet_labels_dict)
