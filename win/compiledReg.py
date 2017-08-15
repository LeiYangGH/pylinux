import re
s = "hell asdfasdf asdfas asdfawef asd adsfas " 
reObj1 = re.compile('((\w+)\s+\w+)') 
all = reObj1.findall(s)
print all
