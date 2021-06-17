import pandas as pd
import re

table1 = pd.read_html("https://www.tutorialrepublic.com/html-reference/html5-tags.php")[0]

table1["Tag"] = table1["Tag"].apply(lambda x: re.sub("<|>", "", x))
table1["Description"] = table1["Description"].apply(lambda x: x.split()[0])
table1["Check"] = table1["Description"]
table1["Check"] = table1["Check"].apply(lambda x: 0 if x == "Obsolete" else 1)
table1 = table1[table1["Check"] == 1]

file = open("keywords1.txt", "r+")
file.truncate(0)
file.close()

f = open('keywords1.txt', 'w')
for ele in table1["Tag"]:
    f.write(ele+'\n')

table2 = pd.read_html("https://www.tutorialrepublic.com/css-reference/css3-properties.php")[0]

file = open("keywords2.txt", "r+")
file.truncate(0)
file.close()

f = open('keywords2.txt.txt', 'w')
for ele in table2["Property"]:
    f.write(ele+'\n')