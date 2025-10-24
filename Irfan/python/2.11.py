#accept a file name from the user and then print the extension
import os

filename = input("Enter the file name: ")
_, extension = os.path.splitext(filename)

if extension:
    print("The extension of the file is:", extension[1:])  # remove the dot
else:
    print("No extension found in the file name.")
