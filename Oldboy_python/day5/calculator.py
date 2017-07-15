#!/usr/bin/env python3
#coding:utf-8
import re

def handle_sub_div_occactions(plus_and_minus_operators, mut_sub_list):
    '''处理1*-2这种特殊形式'''
    for index,x in enumerate(mut_sub_list):
        x = x.strip()
        if x.endswith('*') or x.endswith('/'):
            mut_sub_list[index] = mut_sub_list[index] + plus_and_minus_operators[index] \
                            + mut_sub_list[index+1]
            del plus_and_minus_operators[index]
            del mut_sub_list[index+1]

    return plus_and_minus_operators,mut_sub_list

def remove_duplicates(famula):
    '''处理多余的符号'''
    famula = famula.replace('+-','-')
    famula = famula.replace('-+','-')
    famula = famula.replace('--','+')
    famula = famula.replace('- -','+')
    famula = famula.replace('++','+')
    return famula

def compute_mut_sub(famula):
    """乘除运算"""
    oporators = re.findall('[*/]',famula)
    cal_list = re.split('[*/]',famula)
    res = None
    for index,x in enumerate(cal_list):
        if res:
            if oporators[index - 1] == '*':
                res *= float(x)
            elif oporators[index - 1]  == '/':
                res /= float(x)
        else:
            res = float(x)
    return res


def compute(famula):                                 #(-1 * -2 + -3)
    '''计算括号中的结果并返回'''
    famula = famula.strip('()')                      #-1 *- 2 + -3
    famula = famula.replace(' ','')                  #-1*-2+-3
    famula = remove_duplicates(famula)               #-1*-2-3
    compute_list = re.split('[+-]',famula)           #['1*','2','3']
    plus_and_minus_operators = re.findall('[+-]',famula)  #['-','-','-']
    if len(compute_list[0].strip()) == 0:  # 代表这肯定是个减号
       compute_list[1] = plus_and_minus_operators[0] + compute_list[1]
       del compute_list[0]
       del plus_and_minus_operators[0]                 #['-1*','2','3']

    plus_and_minus_operators,compute_list = handle_sub_div_occactions(plus_and_minus_operators, compute_list)  #['-1*2','3']
    for index,x in enumerate(compute_list):
        if re.search('[*/]',x):
            compute_list[index] = compute_mut_sub(x)   #处理完毕可以带入函数计算

    print(compute_list,plus_and_minus_operators)
    #加减运算
    total_re = None
    for index, x in enumerate(compute_list):
        if total_re:
            if plus_and_minus_operators[index - 1] == '+':
                total_re += float(x)
            elif plus_and_minus_operators[index - 1] == '-':
                total_re -= float(x)
        else:
            total_re = float(x)
    return total_re

def cal(expression):
    parenthesise_flag = True
    while parenthesise_flag:
        m = re.search(r'\([^()]+\)',expression)
        if m :
            print('计算括号%s的值' % m.group())
            res = compute(m.group())
            expression = expression.replace(m.group(),str(res))
        else:
            print('括号已经取完，输出结果:',compute(expression))
            parenthesise_flag = False

if __name__ == '__main__':
    s = '1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
    cal(s)

