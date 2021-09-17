"""
In this code I'm removing duplicity from one file versus another file based on three premises:

1. The comparison must only occur between the characters determined in the begin_pos_compare and end_pos_compare variables

2. The initial 2 characters of the line must start with the value defined in item_file_delimiter

3. When you find a duplicate and if the previous line starts with the value defined in the variable header_file_delimiter, this line must also be deleted
"""

import time
import itertools

def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)

f1_name = input("File 1: ")
f2_name = input("File 2: ")
fs_name = input("File Exit: ")

begin_pos_compare = 67
end_pos_compare = 128

header_file_delimiter = "R0"
item_file_delimiter = "R1"


with open(f1_name, 'r') as f1, open(f2_name, 'r') as f2:
    a = f1.readlines()
    b = f2.readlines()

for previous, current  in pairwise(b):
    if current[0:2] == item_file_delimiter:
        for element_a in a:    
            if(current[begin_pos_compare:end_pos_compare] == element_a[begin_pos_compare:end_pos_compare]):
                    if previous[0:2] == header_file_delimiter:
                        b.remove(previous)
                        b.remove(current)
                    else:
                        b.remove(current)

#non_duplicates = [line for line in b if line not in a]

f = open(fs_name, 'w')
for element in b:
    f.write(element)
f.close()
