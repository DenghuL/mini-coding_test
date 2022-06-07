#!/usr/bin/env python
# -*- coding:utf-8 -*-

def my_input(target)->list :
    '''判断输入是否是0-9'''
    try:
        str1=input('input("q" is quit): ')
        if str1=='q':return False
        str=eval(str1)
        for i in str:
            if i not in target:
                print('请输入0~9的数字,用","隔开')
                return []
        return str
    except Exception:
        print('--输入格式:[0] --')
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
        if input_n==False:break#结束输入
        #处理输入
        solution(input_n,data)