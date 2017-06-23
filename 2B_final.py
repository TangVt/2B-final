import sys
import os
import numpy as np
import string
import csv

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
    with open(path, 'r') as csvfile:
        rd = csv.reader(csvfile)
        for row in rd:
            #print(row)
            temp.append(row)
    csvfile.close()
    return temp

def write_SusList(path, list):
    with open(path, 'w') as csvfile:
        fieldnames = ['vendor', 'metal']
        wt = csv.DictWriter(csvfile, fieldnames = fieldnames)
        wt.writeheader()
        for i in range(len(list)):
            wt.writerow({'vendor': list[i][0], 'metal': list[i][1]})
    csvfile.close()
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
    lr = load_result(result_path)[0]
    #drd = csv.DictReader(open(VenList_path, 'r'))
    result_loc = lr[0]
    print(len(lr))
    print(lr)
    for i in range(len(lr)-1):
        result_metal = lr[i+1]
        print('Now water is polluted by {0}'.format(result_metal))
        drd = csv.DictReader(open(VenList_path, 'r'))
        for row in drd:
            #print row
            if (row['location'] == result_loc) and (row['metal'] == result_metal):
                print('Suspect: {0}, {1}'.format(row['vendor'], row['metal']))
                Suslist.append([row['vendor'], row['metal']])
                #print(Suslist)
        #drd.clear()
#
        write_SusList(SusList_path, Suslist)