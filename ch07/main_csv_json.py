#!/usr/bin/env python
from pprint import pprint
import json
import csv
def main_old():
    customers = []
    
    with open("MOCK_DATA.csv") as f:
        lines = [line.strip() for line in f.readlines()]
        keys = lines[0].split(',')
        data = lines[1:]
        
        for line in data:
            customer = line.split(',')
            d = zip(keys,customer)
            customers.append(dict(d))
        
    with open("customers.json","w") as f:
        json.dump(customers,f)


def main():
    customers = []
    with open('MOCK_DATA.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            customers.append(row)
    
    with open("customers.json","w") as f:
        json.dump(customers,f)

if __name__ == '__main__':
    main()



