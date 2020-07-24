#!/usr/bin/python3
import sys
import os
import pandas as pd


def get_size(path):  # Function to determine directory size
    total = 0
    for entry in os.scandir(path):
        try:
            if entry.is_dir(follow_symlinks=False):
                total += get_size(entry.path)
            else:
                total += entry.stat(follow_symlinks=False).st_size  # Gives File size
        except Exception as e:
            print("Exception :", e)
            total += 0
    return total


if __name__ == '__main__':
    path = '/home'
    print("Total Arguments Passed :",
          len(sys.argv))  # If output is 1 that means the first argument on command line is program itself
    # if you pass /home as other argument the output would be 2
    directory = sys.argv[1] if len(sys.argv) >= 2 else path
    usage = []  # list of disk usage
    paths = []  # list of directory path
    for entry in os.scandir(directory):  # Gives all the subdirectories & Files underneath directory
        print(entry.path)  # Printing Full Path Name
        if entry.is_dir(follow_symlinks=False):  # Ignoring Symbolic Links
            # print(entry.path + " is a directory")
            # print(get_size(entry.path))
            total = get_size(entry.path)
            print(total)
            paths.append(entry.path)
            usage.append(total)
        usage_dict = {' directory ': paths, ' usage ': usage}
        df = pd.DataFrame(usage_dict)
        print(df)
        df.to_csv("Disk_Report.csv")
