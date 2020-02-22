# coding=utf-8
import os
import requests
import re
import json

from startup import MatchList
class MatchList:
    real_index_id = -1
    name = None
    header = {}
    data = {}
    def __init__(self,index,name,header,data):
        """MatchList类初始化"""
        print("初始化已经完成")
        self.real_index_id = index
        self.name = name
        self.header = header
        self.data = data
def dvstr(r):
    barr = bytearray();
    rlen = len(r);
    i = 0;
    while i < rlen:
        if r[i] == '\\' and r[i+1] == 'x':
            barr.append(ord(r[i+2]))
            barr.append(ord(r[i+3]))
            i+=4;
        else:
            hexc = hex(ord(r[i]))
            barr.append(ord(hexc[2]))
            barr.append(ord(hexc[3]))
            i+=1;
    hexstr = str(barr,'utf-8');
    return bytes.fromhex(hexstr).decode('utf-8')
def get_data(url,header,data):
    response = requests.post(url,header,data)
    # str = dvstr(response.content)
    print(response.content)
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
    f = open('/Users/plantkon/PycharmProjects/zhuabaodemo/release/targetd/1.txt')
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
    h1 = {"Host": "ssl.kohsocialapp.qq.com:10001", "Content-Type": "application/x-www-form-urlencoded", "Accept-Encoding": "br,gzip,deflate", "Cookie": "pgv_pvid=5457054890;pgv_pvi=3969268736;eas_sid=u1I5h738S2D27572c8D8M1K0y0", "Connection": "keep-alive", "Accept": "*/*", "User-Agent": "smoba/3.46.202(iPhone;iOS12.3.1;Scale/2.00)", "Accept-Language": "zh-Hans-CN;q=1,zh-Hant-CN;q=0.9,ko-KR;q=0.8", "noencrypt": "1", "Content-Length": "697"}
    matchlist = scan_dic()
    print(matchlist.header)
    print(matchlist.data)
    get_data('https://ssl.kohsocialapp.qq.com:10001/play/getmatchlist',h1,matchlist.data)

main()