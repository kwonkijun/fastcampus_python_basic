import csv

file = open("./myvenv/Chapter10/student.csv", "r", encoding="utf-8-sig")
reader = csv.reader(file)
for data in reader:
    print(data)
file.close()