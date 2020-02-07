import csv
import time

with open('example.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        print('{:<15} {:15} {:<20} {:25}'.format(*line))
        time.sleep(0.1)