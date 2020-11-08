import spacy
import csv
import pandas as pd
import random
input_list = []
with open('test.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        input_list.append(row[0].split("\t"))
        # print(row[0].split("\t"))
nlp = spacy.load('en_core_web_lg')
for i in range(0,120):
    syn_list = "Amazing	Incredible Unbelievable Improbable Astonishing Beautiful Gorgeous Dazzling Splendid Magnificent".split(" ")
    print(nlp(random.choice(syn_list)).similarity(nlp(random.choice(syn_list))))
print("*******************************************************************")
for i in range(0,120):
    syn_list = "Absence	Presence Plenty	Existence Enough Accept	Refuse Fail Deny Reject".split(" ")
    print(nlp(random.choice(syn_list)).similarity(nlp(random.choice(syn_list))))
print("*******************************************************************")
for i in range(0,120):
    syn_list = "Amazing	Incredible Unbelievable Improbable Astonishing Beautiful Gorgeous Dazzling Splendid Magnificent".split(" ")
    ant_list = "Absence	Presence Plenty	Existence Enough Accept	Refuse Fail Deny Reject".split(" ")
    print(nlp(random.choice(syn_list)).similarity(nlp(random.choice(ant_list))))
print("*******************************************************************")
print(nlp('fat').similarity(nlp('fool')))
print("*******************************************************************")
column = ['p1','p2','p3','p4','p5','p6']
index = ['c'+str(index) for index in range(1, len(input_list)+1)]
df = pd.DataFrame(input_list, columns=column, index=index)
print(df)
def check_boundry(row):
    for key, _val in row.items():
        if float(row[key]) >= 0.75:
            row[key] = 1
        else:
            row[key] = 0
    return row
print("*******************************************************************")
df = df.apply(lambda row: check_boundry(row),axis=1)
print(df)
print("*******************************************************************")
df['estimatedAvg'] = df.apply(lambda row: sum(list(row.values))/len(list(row.values)),axis=1)
print(df)
print("*******************************************************************")
df['estimatedSim'] = df.apply(lambda row: 1 if row['estimatedAvg'] >= 0.60 else 0,axis=1)
print(df)