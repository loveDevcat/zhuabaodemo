# coding=utf-8
import os
import requests
import re
import json

from startup import MatchList


def get_data(url,header,data):
    response = requests.post(url,header,data)

    print (response.text)

def scan_dic():
    matchlist = MatchList(1,1,1,1)
    index = 1
    box = None
    target_dic = os.getcwd() + '/targetd'
    print(target_dic)
    backup_dic = os.getcwd() + '/backupd'

    files = os.listdir(target_dic)
    for file in files:
       box =  str_to_json(file)
       matchlist.header = box[2]
       matchlist.data = box[1]

    return matchlist


def str_to_data(str):
    r = {}
    list = str.split('&')
    for item in list:
        re_list = item.split('=')
        r[re_list[0]] = re_list[1]
    # print(type(r))
    # print(r)
    # r = list()
    # r.append('{"')
    # for index in range(len(str)):
    #     if (str[index] == '='):
    #         r.append('"')
    #         r.append(':')
    #         r.append('"')
    #     elif (str[index] == '&'):
    #         r.append('"')
    #         r.append(',')
    #         r.append('"')
    #     else:
    #         r.append(str[index])
    # r.append('"}')

    return r


def str_to_json(filename):
    header_buffer = {}
    r = None
    print('文件开始读')
    # f = open('/Users/plantkon/PycharmProjects/zhuabaodemo/10.txt','r',encoding='utf-8')

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
    h1 = {"Host": "ssl.kohsocialapp.qq.com:10001", "Content-Type": "application/x-www-form-urlencoded", "Accept-Encoding": "br,gzip,deflate", "Cookie": "pgv_pvid=5457054890;pgv_pvi=3969268736;eas_sid=u1I5h738S2D27572c8D8M1K0y0", "Connection": "keep-alive", "Accept": "*/*",
          "User-Agent": "smoba/3.46.202(iPhone;iOS12.3.1;Scale/2.00)", "Accept-Language": "zh-Hans-CN;q=1,zh-Hant-CN;q=0.9,ko-KR;q=0.8", "noencrypt": "1", "Content-Length": "696"}
    d1 = {"apiVersion":"3","cChannelId":"0","cClientVersionCode":"2019101809","cClientVersionName":"3.46.202","cCurrentGameId":"20001","cDeviceCPU":"ARM64",
          "cDeviceId":"eb51be8d777cf88fe561c08eb6a9bb9e3fde35e8","cDeviceIdfa":"0AECED4C-0439-44FB-9894-0417A68EA543","cDeviceMem":"2086879232","cDeviceModel":"iPhone","cDeviceNet":"WiFi","cDeviceSP":"%E4%B8%AD%E5%9B%BD%E7%94%B5%E4%BF%A1",
          "cDeviceScreenHeight":"667","cDeviceScreenWidth":"375","cGameId":"20001","cGzip":"1","cRand":"1582371965712","cSystem":"ios","cSystemVersionCode":"12.3.1","cSystemVersionName":"iOS","friendUserId":"90873130","gameAreaId":"2","gameId":"20001","gameOpenId":"8AD687FC68C4650858AA1A6CC166AAF6",
          "gameRoleId":"106588992","gameServerId":"2055","gameUserSex":"0","isMI":"0","lastTime":"0","option":"0","roleId":"106588992","token":"3dkw46eN","userId":"90873130"}

    tem = matchlist.data

    # print(matchlist.data)
    response = requests.post("https://ssl.kohsocialapp.qq.com:10001/play/getmatchlist", headers=h1, data=matchlist.data)
    print(response.text)
    # get_data('https://ssl.kohsocialapp.qq.com:10001/play/getmatchlist',h1,matchlist.data)

main()