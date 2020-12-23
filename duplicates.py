import csv
from fnmatch import fnmatch as fm
import os
import pandas as pd


def find(extension, path, csv_file):
    with open(csv_file, 'w', newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Path", "Size"])
        for root, dirs, files in os.walk(path):
            for name in files:
                if fm(name, extension):
                    file_size = round(os.path.getsize(
                        root + "\\" + name) / (1024 * 1024), 2)
                    writer.writerow([name, root, file_size])
    return pd.read_csv(csv_file)


def print_duplicates(file, csv_file):
    file["Duplicate"] = file.duplicated("Name", keep=False)
    duplicates = file[file["Duplicate"] == True]
    duplicates = duplicates.sort_values(by=["Name"])
    duplicates.to_csv(csv_file, index=False, encoding="utf-8")
    print(duplicates.to_string())


def delete_logs(logs):
    if os.path.exists(logs):
        os.remove(logs)


def main():
    extension = '*.mp3'
    path = ".\\Test Folder"
    csv_file = 'my_mp3s.csv'
    file = find(extension, path, csv_file)
    print_duplicates(file, csv_file)
    return csv_file


def loop():
    while True:
        logs = main()
        runagain = input("Run again? (y or n) ")
        if runagain != 'y':
            delete_logs(logs)
            print("Thanks!!")
            break


loop()
