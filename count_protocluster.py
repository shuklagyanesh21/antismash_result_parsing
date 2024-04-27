import glob
from Bio import SeqIO
from collections import Counter
import pandas as pd
import os

file_directory = "/home/gyanesh/myxo_87/antismash_result/as_result_complete/"
gfiles = glob.glob(file_directory + "/**/*genomic.gbk", recursive=True)
print("Files to be processed=", len(gfiles))

def read_file(gfile):
    products = []
    for record in SeqIO.parse(gfile, 'gb'):
        for feature in record.features:
            if feature.type == 'protocluster':
                for qualifier in feature.qualifiers.get('product', []):
                    products.append(qualifier)
    return products

def count_products(product_list):
    product_count = Counter(product_list)
    return product_count

def scan_all_products(files):
    all_products = set()
    for gfile in gfiles:
        products = read_file(gfile)
        all_products.update(products)
    all_products = list(all_products)
    print('All unique products have been identified')
    return all_products

all_products = scan_all_products(gfiles)

all_product_count = []

for gfile in gfiles:
    directory, filename = os.path.split(gfile)
    filename = filename.strip('_genomic.gbk')
    products = read_file(gfile)
    product_count = count_products(products)
    temp_count = []

    temp_count.append(filename)

    for product in all_products:
        if product in product_count.keys():
            temp_count.append(product_count[product])
        else:
            temp_count.append(0)
    all_product_count.append(temp_count)

columns = ['File'] + all_products

dataframe = pd.DataFrame(all_product_count, columns=columns)
dataframe.set_index('File', inplace=True)

outputfile = '/home/gyanesh/myxo_87/antismash_result/as_product_count.csv'

dataframe.to_csv(outputfile, index=True)
