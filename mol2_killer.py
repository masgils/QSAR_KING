#!/usr/bin/env
# coding: utf-8

#更改mol2文件中的原子编排方式

import os
        
def mol2change(fileName):
    '''改写antechamber生成的mol2文件中的原子编号'''

    with open(fileName) as f:
        text = f.readlines()


    newline = []


    currentLine = 8
    line = text[currentLine]

    #mol2文件前8行
    for i in text[:currentLine]:
        newline.append(i)

    #mol2文件ATOM部分
    count = 1
    while line.split()[0] != '@<TRIPOS>BOND':
        #重新按顺序编排原子序号
        g = line.split()
        new = ''
        for j in g[1]:
            if j.isalpha() != 0:
                new += j
        
        g[1] = new + str(count)
        count += 1        
        newline.append('    '.join(g) + '\n')
        currentLine += 1
        line = text[currentLine]

    #mol2文件剩余部分
    for k in text[currentLine:]:
        newline.append(k)

    q = open(fileName,'w')
    q.writelines(newline)
    q.close()

def run():    
    path = os.listdir(os.getcwd())

    for file in path:
        if '.mol2' in file:
            mol2change(file)
        
if __name__ == '__main__':
    run()

