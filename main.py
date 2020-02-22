# coding=utf-8
import os
import requests
import re
import json

from startup import MatchList


def get_data(url,header,data):
    response = requests.post(url,header,data)

    print (response.text)
    # return response.text

def scan_dic():
    index = 1
    box = None
    target_dic = os.getcwd() + '/targetd'
    # os.chdir(target_dic)
    backup_dic = os.getcwd() + '/backupd'

    files = os.listdir(target_dic)
    for file in files:
       box =  str_to_json(file)
       matchlist = MatchList(index,box[0],box[2],box[1])
       print(matchlist.header)
       print(matchlist.data)
    return matchlist


def str_to_data(str):
    r = list()
    r.append('{"')
    for index in range(len(str)):
        if (str[index] == '='):
            r.append('"')
            r.append(':')
            r.append('"')
        elif (str[index] == '&'):
            r.append('"')
            r.append(',')
            r.append('"')
        else:
            r.append(str[index])
    r.append('"}')

    return ''.join(r)


def str_to_json(filename):
    header_buffer = {}
    r = None
    print('文件开始读')
    f = open('/Users/plantkon/PycharmProjects/zhuabaodemo/2.txt')
    line = f.readline()
    url = (re.findall(r'[a-zA-z]+://[^\s]*', line))
    flag = 0
    while 1:
        line = f.readline()
        if '###' in line:
            flag = flag + 1
        if (flag != 2):
            # print(line)
            if 'apiVersion' in line:
                r = str_to_data(line)
                # R = r
                # print(r)
            elif (':' in line and flag == 1 and '###' not in line):
                clear_line = line.replace('\n','').replace(' ','')
                x = clear_line.split(':')
                header_buffer[x[0]] = x[1]

        if (flag == 2):
            break
    f.close()
    header_json = json.dumps(header_buffer)
    box = (url,r,header_json)
    return box
def main():
    matchlist = scan_dic()
    print(matchlist.header)
    print(matchlist.data)
    get_data('https://ssl.kohsocialapp.qq.com:10001/play/getmatchlist',matchlist.header,matchlist.data)

main()