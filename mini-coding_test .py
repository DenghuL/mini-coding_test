#!/usr/bin/env python
# -*- coding:utf-8 -*-

def my_input(target)->list :
    '''判断输入是否是0-9'''
    try:
        str1=input('input("q" is quit): ')
        if str1=='q':return False
        str=eval(str1)
        for i in str:
            if i not in range(0,100):
                print('请输入0~99的数字,用","隔开')
                return []
        return str
    except Exception:
        print('--输入数字为列表格式:[0] --')
        return []

def solution(input_n,data):
    '''根据输入数字，将数字代表的字母进行组合'''
    # 临时变量
    temp = []
    # 接受结果变量
    res = []
    for i in input_n:
        if res==[]:
            res=data[i]
        else:
            for j in res:
                for k in data[i]:
                    #临时变量接收最新结果
                    temp.append(j+k)
            res=temp
            temp=[]
    #输出结果
    print('Output: ' + ' '.join(res))

def digit_converting_letter(num):
    '''0-99数字转换字符'''
    co_str=chr(num)
    print(f'converting: {num} is {co_str}')
if __name__ == '__main__':
    #初始化[0~9]代表的字母
    data={
        0:[],
        1:[],
        2:['a','b','c'],
        3:['d','e','f'],
        4:['g','h','i'],
        5:['j','k','l'],
        6:['m','n','o'],
        7:['p','q','r','s'],
        8:['t','u','v'],
        9:['w','x','y','z']
          }
    while True:
        #接受输入
        input_n=my_input(data.keys())
        solu_n=[]
        if input_n==False:break#结束输入
        #处理输入
        for j in input_n:
            if j in data.keys():
                solu_n.append(j)
        #将0-9数字代表字母组合
        solution(solu_n,data)
        #0-99转换为字符
        for i in input_n:
            digit_converting_letter(i)