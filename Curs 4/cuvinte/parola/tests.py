from django.test import TestCase

# Create your tests here.
# print(ord('A')) #cod ascii 65 - dif de 32 pana la a mic
# print(ord('B')) #cod ascii 66
# print(ord('C')) #cod ascii 67

# print(ord('Z')) #cod ascii 90 - dif de 32 pana la z mic

# print(ord('a')) #cod ascii 97
# print(ord('z')) #cod ascii 122

# print(chr(65))
# print(chr(122))

# for i in range (ord('A'), ord('Z')+1):
#     print(chr(i))

import pandas as pd

with open("parole.csv", "w") as fwriter:    
    fwriter.write("parole")

df = pd.read_csv("parole.csv")
print(df)
df.to_json("parole.json")
print(df)