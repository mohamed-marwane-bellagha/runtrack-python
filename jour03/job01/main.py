import xml.etree.ElementTree as ET
import re
tree = ET.parse('domains.xml')
root = tree.getroot()
# print(tree)
caca = root.findall("./database/table/column")
# for pipi in caca:
#     print(pipi.attrib)
arr = []
for child in root:
    database = child
    for child in database:
        table = child
        for neighbor in table.iter('column'):
            if "domain" in neighbor.attrib['name']:
                text=neighbor.text
                new_string = text.split(".")[1]
                arr.append(new_string)
                # print(new_string)

# print(arr)
result = []
for i in arr:
    if i not in result:
        result.append(i)
for i in result:
    print(i)