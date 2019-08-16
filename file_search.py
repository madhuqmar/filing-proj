#!/usr/local/bin/python3

from os import listdir
from os.path import isfile, join

#set base path
mypath = "/Users/madhukumar"

# Ask the user to enter which directory, file type and search string
search_path = input("Enter directory path to search: ")
file_type = input("Enter file type: ")
search_str = input("Enter the search string: ")

#join the base path and the input search pach
real_path = join(mypath, search_path)

#filter files in the complete search path
onlyfiles = [f for f in listdir(real_path) if isfile(join(real_path, f))]

#filter files with the specified file type and string in filename
for i in onlyfiles:
	if i.endswith(file_type):
		if search_str in i:
			print(i)