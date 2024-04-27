import glob
from Bio import SeqIO
from collections import Counter
import pandas as pd
import os

file_directory="/home/gyanesh/myxo_87/antismash_result/as_result_complete/"
gfiles = glob.glob(file_directory + "/**/*genomic.gbk", recursive=True)

#gfiles=glob.glob("%s/*genomic.gbk"%file_directory, recursive=True)          #forms a list of filespaths
print("Files to be processed=",len(gfiles))

def read_file(gfile):
    features = []
    for record in SeqIO.parse(gfile, 'gb'):
        features.extend([feature.type for feature in record.features])
    return features


def count_features(feature_types):
    feature_count=Counter(feature_types)
    return feature_count

def scan_all_features(files):
    allfeatures=[]
    for gfile in gfiles:
        feature_types=read_file(gfile)
        allfeatures.extend(feature_types)           #extend add the values of list in a new list, .append would have create list in list

    allfeatures=set(allfeatures)                    #creating a set is import to remove duplicates before converting to list again
    allfeatures=list(allfeatures)
    print('All features have been identified')
    return allfeatures

allfeatures=scan_all_features(gfiles)

print(allfeatures)

allfeature_count=[]

for gfile in gfiles:
    directory,filename=os.path.split(gfile)
    filename=filename.strip('_genomic.gbk')
    feature_types=read_file(gfile)
    feature_count=count_features(feature_types)
    temp_count=[]

    temp_count.append(filename)
   
    for feature in allfeatures:
        if feature in feature_count.keys():
            temp_count.append(feature_count[feature])
        else:
            temp_count.append(0)
    allfeature_count.append(temp_count)

print(allfeatures)

columns=[]
columns.append('File')
columns.extend(allfeatures)

dataframe=pd.DataFrame(allfeature_count,columns=columns)
print(dataframe)

dataframe.set_index('File',inplace=True)

outputfile='/home/gyanesh/myxo_87/antismash_result/as_feature_count.csv'

dataframe.to_csv(outputfile,index=True)
