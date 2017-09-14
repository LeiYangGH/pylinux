from os import walk
import os

def get_all_txts(dir):
    files = {}
    for (dirpath, dirnames, filenames) in walk(dir):
        txts = {fn:os.path.join(dirpath, fn) for fn in filenames if os.path.splitext(fn)[1]=='.txt'}
        files.update(txts)
    return files



def join_txts(files, joinfile):
    with open(joinfile,'wt',encoding='utf-8') as j:
         for (filename,fullname) in files.items():
             try:
                 #print(fullname)
                 fh = open(fullname, 'r',encoding='utf-8')
                 content = fh.read()
                 j.write("="*20+filename+"="*20+"\r\n"*2+"\n")
                 j.writelines(content)
                 j.write( "\r\n" * 2)
             except UnicodeDecodeError as ex:
                 print(fullname)
                 print(ex)
                 pass

             finally:
                 fh.close()
cwd=os.getcwd()
jfile=os.path.join(cwd,'joinfile.txt')
def search_join_txts(dir=cwd,joinfile=jfile):
    logs=get_all_txts(dir)
    join_txts(logs, joinfile)
    print('\nfound %d txt files and joined to %s' % (len(logs), joinfile))

import argparse

parser = argparse.ArgumentParser(description=
                                 'Search all txt files under given directory recursively'
                                 'and combine their contents to one single txt file.'
                                 'if the directory name not specified, the default directory'
                                 'will be current directory;'
                                 'if the target txt file name not specified, the default name'
                                 'will be joinfile.txt under current directory.')
parser.add_argument('dir',default=cwd, nargs='?',
                   help='directory to search txt files')
parser.add_argument('joinfile',default=jfile, nargs='?',
                   help='txt file name to join contents to')

args = parser.parse_args()
print(args.dir)

if __name__ == '__main__':
    search_join_txts(args.dir,args.joinfile)