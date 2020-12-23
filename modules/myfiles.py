from fnmatch import fnmatch as fm
import os
import pandas as pd


def MyTable(extension, path):
    myfiles = pd.DataFrame(columns=['Name', 'Size', 'Path'])
    for root, dirs, files in os.walk(path):
        for name in files:
            if fm(name, extension):
                file_size = round(os.path.getsize(
                    root + "\\" + name) / (1024 * 1024), 2)
                myfiles = myfiles.append({"Name": name, "Size": str(
                    file_size), "Path": root}, ignore_index=True)
                myfiles["Duplicate"] = myfiles.duplicated("Name", keep=False)
    duplicates = myfiles[myfiles["Duplicate"] == True]
    duplicates = duplicates.sort_values(by=["Name"])
    return duplicates

