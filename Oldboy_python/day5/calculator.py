#!/usr/bin/env python3
#coding:utf-8
import re

def compute_mut_sub(famula):
    """乘除运算"""
    oporators = re.findall('[*/]',famula)
    cal_list = re.split('[*/]',famula)
    res = None
    for index,x in enumerter(cal_list):
        if res:
            if oporators[index - 1] == '*':
                res *= float(x)
            elif oporators[index - 1]  == '/':
                res /= float(x)
        else:
            res = float(res)
    return res
def compute_add_sub():
    """加减运算"""
    oporators = re.findall('[+-]', famula)
    cal_list = re.split('[+-]', famula)
    res = None
    for index, x in enumerter(cal_list):
        if res:
            if oporators[index - 1] == '+':
                res *= float(x)
            elif oporators[index - 1] == '-':
                res /= float(x)
        else:
            res = float(res)
    return res

def compute(famula):
    '''计算括号中的结果并返回'''
    famula = famula.strip('()')
    famula = famula.replace(' ','')
    mut_sub_list = re.split('[+-]',famula)  #5+6+6/7*c

    compute_mut_and_sub = compute_mut_sub(mut_sub_list)
    pass


def cal(expression):
    parenthesise_flag = True
    while parenthesise_flag:
        m = re.search(r'\([^()]+\)',expression).group()
        if m :
            res = compute(m)
            expression = expression.replace(m,str(res))
        else:
            print('括号已经取完，输出结果:',compute(expression))
            parenthesise_flag = False
if __name__ == '__main__':
    s = '1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
    cal(s)

