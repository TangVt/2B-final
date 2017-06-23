import sys
import os
import numpy as np
import string

###############
## variables ##
###############
result_path = sys.argv[1]
VenList_path = sys.argv[2]
SusList_path = sys.argv[3]
result_loc = ''
result_metal = ''
Suslist = []
#############
## utility ##
#############

def load_result(path):
    temp = []
    with open(path, 'r', encoding='utf-8') as csvfile:
        rd = csv.reader(csvfile)
        for row in reader:
            print(row)
            temp.append(row)
    csvfile.close()
    return temp

def write_SusList(path, list, metal):
    with open(path, 'w', encoding='utf-8') as csvfile:
        fieldnames = ['vendor', 'metal']
        wt = csv.DictWriter(csvfile, fieldnames = fieldnames)
        wt.writeheader()
        for i in range(len(list)):
            wt.writerow({'vendor': list[i], 'metal': metal})
'''
def load_SuspectList(path)
    temp = []
    suspect = []
    with open(path, 'r', encoding='utf-8') as csvfile:
        drd = csv.DictReader(csvfile)

        for row in drd:
            temp.append(row[location])
            temp.append(row[vendor])
            temp.append(row[metal])
            suspect.append(temp)
            temp.clear()
    csvfile.close()

   return suspect

'''

###################
## Main function ##
###################
if __name__=='__main__':
    lr = load_result(result_path)
    result_loc = lr[0]
    result_metal = lr[1]

    drd = csv.DictReader(open(VenList_path, 'r', encoding='utf-8'))
    for row in drd:
        if (row[location] == result_loc) and (row[metal] == result_metal):
            Suslist.append(row[vendor])
#
    write_SusList(SusList_path, Suslist, result_metal)