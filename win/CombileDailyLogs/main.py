from os import walk
import re
import os

def get_all_logs(dir):
    f = {}
    for (dirpath, dirnames, filenames) in walk(dir):
        logs = {fn:os.path.join(dirpath, fn) for fn in filenames if re.match(r'\d{4}-\d{2}-\d{2}.txt$', fn) is not None}
        f.update(logs)
    #f.sort(key=lambda x:x.key)
    return f

def join_logs(logs,allfile):
    with open(allfile,'wt',encoding='utf-8') as all:
         for (filename,fullname) in logs.items():
             try:
                 print(fullname)
                 logf = open(fullname, 'r',encoding='utf-8')
                 content = logf.read()
                 all.write("="*20+filename+"="*20+"\r\n"*2+"\n")
                 all.writelines(content)
                 all.write( "\r\n" * 2)
             except UnicodeDecodeError:
                 print(fullname)
                 pass

             finally:
                 logf.close()


logs=get_all_logs(r'C:\0Task')
print(len(logs))
join_logs(logs,r'C:\0Task\all.txt')
print('done')