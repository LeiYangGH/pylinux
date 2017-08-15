#!/usr/bin/env python
# coding: UTF-8
import csv
my_file = r'C:\test\test.csv'
with open(my_file) as f:
  reader = csv.reader(f)
  row1 = next(reader)
print(row1)
print(row1[0])
print('hello')




