import re
input = r'sdf)*&^%jlk,.,sd中文——2384中文sldfe#$%^&*ejfk'
words = re.findall(r'[\u4E00-\u9FA5]+.*[\u4E00-\u9FA5]+', input)
print (words)

