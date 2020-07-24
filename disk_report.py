#!/usr/bin/python3
import sys
import os
if __name__ == '__main__':
    path = '/home'
    print("Total Arguments Passed :", len(sys.argv))  # If output is 1 that means the first argument on command line is program itself
    # if you pass /home as other argument the output would be 2
    directory = sys.argv[1] if len(sys.argv) >= 2 else path
    for entry in os.scandir(directory): #Gives all the subdirectories & Files underneath directory
        print(entry.path) #Printing Full Path Name
        if entry.is_dir(follow_symlinks=False): #Ignoring Symbolic Links
            print(entry.path + " is a directory")
