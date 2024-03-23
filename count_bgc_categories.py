import glob
from Bio import SeqIO
from collections import Counter
import pandas as pd
import os

file_directory = "/home/gyanesh/myxo_87/antismash_result/as_result_complete/"
gfiles = glob.glob(file_directory + "/**/*genomic.gbk", recursive=True)
print("Files to be processed=",len(gfiles))

def read_file(gfile):
    features = []
    for record in SeqIO.parse(gfile, 'gb'):
        for feature in record.features:
            if 'category' in feature.qualifiers:
                features.extend(feature.qualifiers['category'])
    return features

def count_features(feature_types):
    feature_count = Counter(feature_types)
    return feature_count

def scan_all_features(files):
    allfeatures = set()
    for gfile in gfiles:
        feature_types = read_file(gfile)
        allfeatures.update(feature_types)
    allfeatures = list(allfeatures)
    print('All bgc_categories have been identified')
    return allfeatures

allfeatures = scan_all_features(gfiles)

allfeature_count = []

for gfile in gfiles:
    directory, filename = os.path.split(gfile)
    filename = filename.strip('_genomic.gbk')
    feature_types = read_file(gfile)
    feature_count = count_features(feature_types)
    temp_count = []

    temp_count.append(filename)

    for feature in allfeatures:
        if feature in feature_count.keys():
            temp_count.append(feature_count[feature])
        else:
            temp_count.append(0)
    allfeature_count.append(temp_count)

columns = ['File'] + allfeatures

dataframe = pd.DataFrame(allfeature_count, columns=columns)
dataframe.set_index('File', inplace=True)

outputfile = '/home/gyanesh/myxo_87/antismash_result/as_bgc_category_count.csv'

dataframe.to_csv(outputfile, index=True)

