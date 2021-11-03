import sys
import re
import itertools
import time

input_template_file = sys.argv[1]
input_keyword1_file = sys.argv[2]
input_keyword2_file = sys.argv[3]
start_time = time.time() # Variable used to track amount of time it takes to create a cartesian product

def cartesian_product_generator(templates,keyword1,keyword2): # Primary function used to generate cartesian product
    for elem in itertools.product(keyword1,keyword2):
        for template in template_list:
            yield template.replace('{keyword1}',elem[0]).replace('{keyword2}',elem[1])

def dedupe_list(input_list): # Function removes any duplicate values from master list
    set = {}
    map(set.__setitem__, input_list, [])
    yield set.keys()

def write_file(input_generator,filename): # Function writes cartesian product export file
    with open('2keyword_templates_{0}.txt'.format(filename),'w') as export_file:
        for elem in input_generator:
            for line in elem:
                export_file.write(str(line) + '\n')

with open(input_template_file, 'r') as template_file: # Opens up template input file
    template_list = [template.strip('\n') for template in template_file]
with open(input_keyword1_file, 'r') as input_file1: # Opens up keyword1 input file
    input_list1 = [line.strip('\n') for line in input_file1]
with open(input_keyword2_file, 'r') as input_file2: # Opens up keyword2 input file
    input_list2 = [line.strip('\n') for line in input_file2]

print('Generating keywords... please wait...')
templated_cartesian_product = cartesian_product_generator(template_list,input_list1,input_list2)
print('Removing any duplicates... please wait...')
cartesian_product_final = dedupe_list(templated_cartesian_product)
print('Exporting file... please wait...')
write_file(cartesian_product_final,'cartesian_product')
print('Cartesian product generated.')
print('Creating this cartesian product took',time.time()-start_time,'seconds.') # Time tracking calculation, prints how many seconds cartesian generation takes