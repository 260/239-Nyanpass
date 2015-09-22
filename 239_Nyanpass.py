#!/usr/bin/python3

# This problem is http://yukicoder.me/problems/659

first_line      = input()
num_of_people   = int(first_line)

rows           = []
for i in range(num_of_people):
    rows.append(input().split(' '))

columns         = []
for i in range(num_of_people):
    columns.append([])
    for j in range(num_of_people):
        columns[i].append(rows[j][i])

columns2        = []
for column in columns:
    column.remove('-')
    columns2.append(list(set(column)))

nyanpass_index  = []
for i, column in enumerate(columns2):
    if len(column) == 1 and column[0] == 'nyanpass':
        nyanpass_index.append(i+1)

if len(nyanpass_index) == 1:
    print(nyanpass_index[0])
else:
    print(-1)
