import os
import sys

if len(sys.argv) < 2:
    exit('缺少命令行参数')

if os.path.exists('./newfile.txt'):
    os.remove('./newfile.txt')

newfile = open('./newfile.txt', 'w')
total_lines = 0

def process(path):
    parents = os.listdir(path)
    for parent in parents:
        child = os.path.join(path,parent)
        if os.path.isdir(child):
            process(child)
        else:
            if os.path.isfile(child) and os.path.splitext(child)[1] in ['.js', '.wxml', '.wxss',  '.wxs', '.json', '.wpy']:
                print('合并' + child)
                wirte_file(child)

def wirte_file(file):
    global total_lines

    with open(file, 'r') as f:
        lines = f.readlines()
        total_lines += len(lines)
        newfile.write('          ---------- ' + os.path.split(file)[1]  + ' ----------' + '\n\n')
        for line in lines:
            newfile.write(line)
        newfile.write('\n\n')

path = sys.argv[1]
process(path)
if total_lines > 0:
    newfile.write(f'代码总行数: {total_lines}')

newfile.close()