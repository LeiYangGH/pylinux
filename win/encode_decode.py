import sys

#code = 'utf8'
code = 'gbk'
print ('你好！')
en = '你好！'.encode(code)
print (en);
de = en.decode(code)
print (de);
print ("Hello World!\n");
