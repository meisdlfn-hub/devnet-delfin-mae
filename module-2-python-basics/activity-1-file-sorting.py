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

    files = os.listdir(users)

    image = "Images"
    documents = "Documents"
    videos = "Videos"
    others = "Others"

    print(files)

    for folder in [image, documents, videos, others]:
        folder_path = os.path.join(users, folder)

        if not os.path.exists(folder_path):
            os.mkdir(folder_path)

    for item in files:
        file_path = os.path.join(users, item)

        if os.path.isdir(file_path):
            continue

        extension = os.path.splitext(item)[1].lower()

        if extension in [".jpg", ".jpeg", ".png", ".gif"]:
            destination = image

        elif extension in [".doc", ".docx", ".pdf", ".txt"]:
            destination = documents

        elif extension in [".mp4", ".avi", ".mkv", ".mov"]:
            destination = videos

        else:
            destination = others

        destination_path = os.path.join(users, destination, item)
        shutil.move(file_path, destination_path)

    print("Files sorted successfully.")

else:
    print("Error: Folder does not exist.")


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
One mistake I made was getting confused with my variables, especially when I used the same variable for different things. 
I also had trouble understanding how to get the files from the folder and organize them into different categories. 
From this, I learned that I should use clear variable names and understand what each variable is supposed to store before using it in the code.


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
This can be useful for organizing school files. 
Instead of manually sorting many files into different folders, 
a Python program can do it automatically based on their file type. 
It can save time when there are a lot of files.
"""
