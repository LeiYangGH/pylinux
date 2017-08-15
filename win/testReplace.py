import re

s = '(lol)hello, please help me to clean this table, (smile). thank you!'

out = re.sub('\([^\(\)]+\)','',s)
                
print out;

print "Hello World!\n";
