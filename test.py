import csv
with open("text.csv") as csvfile:
   text = csv.reader(csvfile, delimiter= ",")
   for line in text:
      print(len(line))