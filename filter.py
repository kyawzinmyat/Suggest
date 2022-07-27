import csv

def filter_s():
    with open("words.csv", "r") as file:
        data = csv.reader(file)
        with open("dict.csv", "w+") as new_file:
            for row in data:
                if not "'" in row[0]:
                    new_file.write(row[0] + "\n")

filter_s()