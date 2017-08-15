import xml.etree.ElementTree as ET

tree = ET.parse('path.xml')
root = tree.getroot()
for child in root:
        #print child.tag, child.attrib, child.text
        if str(child.tag) == "path":
            path_str = str(child.text)

print path_str

print 'done'
