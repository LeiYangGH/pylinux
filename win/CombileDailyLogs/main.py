from os import walk
import re
import os

def get_all_logs(dir):
    f = []
    for (dirpath, dirnames, filenames) in walk(dir):
        logs = [(fn,os.path.join(dirpath, fn)) for fn in filenames if re.match(r'\d{4}-\d{2}-\d{2}.txt$', fn) is not None]
        f.extend(logs)
    f.sort(key=lambda x:x[0])
    return f

def join_logs(logs,allfile):
    with open(allfile,'wt',encoding='utf-8') as all:
         for log in logs:
             fullname = log[1]
             try:
                 print(fullname)
                 logf = open(fullname, 'r',encoding='utf-8')
                 content = logf.read()
                 all.write("="*20+log[0]+"="*20+"\r\n"*2)
                 all.writelines(content)
             except UnicodeDecodeError:
                 print(fullname)
                 pass

             finally:
                 logf.close()


logs=get_all_logs(r'C:\0Task')
print(len(logs))
join_logs(logs,r'C:\0Task\all.txt')
print('done')