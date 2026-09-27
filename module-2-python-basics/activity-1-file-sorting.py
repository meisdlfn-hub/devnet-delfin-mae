"""
Module 2 — Activity: File Sorting with os and shutil
Student: Delfin, Cherrie Mae S.
Date: 9/27/2026

============================================
WHAT DID YOU BUILD? (explain in your own words)
============================================
I made a Python program that asks the user to enter a folder path. 
It checks if the folder exists and then gets the files inside it. 
I also made categories for images, documents, videos, and other files. 
The purpose is to organize the files based on their type.


============================================
KEY VOCABULARY
============================================
- os module: A Python module that lets me work with files, folders, and paths.
- shutil module: A Python module that can be used to move, copy, and manage files and folders.
- file path: The location of a file or folder in the computer.
- directory: Another term for a folder where files can be stored.
(add more as needed)


============================================
YOUR SCRIPT
============================================
Paste the code you already wrote for this activity below.
"""

import os
import shutil

users = input("What is your folder path? ")

if os.path.exists(users):
    print("Proceed to Next Step")

    file = os.listdir(users)
    image = 0
    documents = 0 
    videos = 0
    others = 0

    print(file)

    for file in [image, documents, videos, others]:
        if not os.path.exists(file):
            os.mkdir(file)

    for items in file:
        users = os.path.exists(users)

        print (file)
    
else:
    print("Error")


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
One mistake I made was getting confused with my variables, especially when I used the same variable for different things. 
I also had trouble understanding how to get the files from the folder and organize them into different categories.


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional: how is this similar to what real automation scripts do?
think about your own gradebook/attendance workflow — could something
like this save you time there?]
"""
