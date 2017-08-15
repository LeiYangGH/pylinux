import xml.etree.ElementTree
e = xml.etree.ElementTree.parse('x.xml').getroot()
for atype in e.findall('mysqlhost'):
    print(atype.text)
