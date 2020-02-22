#encoding=utf-8
import os
import shutil

from startup import MatchList

i = 0
str = 'apiVersion=3&cChannelId=0&cClientVersionCode=2019101809&cClientVersionName=3.46.202&cCurrentGameId=20001&cDeviceCPU=ARM64&cDeviceId=eb51be8d777cf88fe561c08eb6a9bb9e3fde35e8&cDeviceIdfa=0AECED4C-0439-44FB-9894-0417A68EA543&cDeviceMem=2086879232&cDeviceModel=iPhone&cDeviceNet=WiFi&cDeviceSP=%E4%B8%AD%E5%9B%BD%E7%94%B5%E4%BF%A1&cDeviceScreenHeight=667&cDeviceScreenWidth=375&cGameId=20001&cGzip=1&cRand=1582285217338&cSystem=ios&cSystemVersionCode=12.3.1&cSystemVersionName=iOS&friendUserId=358403327&gameAreaId=2&gameId=20001&gameOpenId=8AD687FC68C4650858AA1A6CC166AAF6&gameRoleId=106588992&gameServerId=2055&gameUserSex=0&isMI=0&lastTime=0&option=0&roleId=118026253&token=UHcG2DJF&userId=90873130'
# l = list()
# l.append('"')
# for index in range(len(str)-1):
#     # if(str[index+1] != '=') or str[index+1] !='&':
#     #     l.append(str[index])
#     if (str[index + 1] == '='):
#         l.append('"')
#         l.append(':')
#         l.append('"')
#     elif(str[index]=='&'):
#         l.append('"')
#         l.append(',')
#         l.append('"')
#
#     elif (str[index] == '='):
#         continue
#     else:
#         l.append(str[index])
# l.append('"')
#
# s = ''
# print(s.join(l))
#
# d = {"apiVersio":"3","cChannelI":"0","cClientVersionCod":"2019101809","cClientVersionNam":"3.46.202","cCurrentGameI":"20001","cDeviceCP":"ARM64","cDeviceI":"eb51be8d777cf88fe561c08eb6a9bb9e3fde35e8","cDeviceIdf":"0AECED4C-0439-44FB-9894-0417A68EA543","cDeviceMe":"2086879232","cDeviceMode":"iPhone","cDeviceNe":"WiFi","cDeviceS":"%E4%B8%AD%E5%9B%BD%E7%94%B5%E4%BF%A1","cDeviceScreenHeigh":"667","cDeviceScreenWidt":"375","cGameI":"20001","cGzi":"1","cRan":"1582281463323","cSyste":"ios","cSystemVersionCod":"12.3.1","cSystemVersionNam":"iOS","friendUserI":"90873130","gameAreaI":"2","gameI":"20001","gameOpenI":"8AD687FC68C4650858AA1A6CC166AAF6","gameRoleI":"106588992","gameServerI":"2055","gameUserSe":"0","isM":"0","lastTim":"0","optio":"0","roleI":"106588992","toke":"SARbRKMg","userI":"9087313"
# }
def str_to_json(str):
    r = list()
    r.append('"')
    for index in range(len(str)):
        if(str[index]=='='):
            r.append('"')
            r.append(':')
            r.append('"')
        elif (str[index]=='&'):
            r.append('"')
            r.append(',')
            r.append('"')
        else:
            r.append(str[index])
    r.append('"')
    return ''.join(r)

# r = str_to_json(str)
# print(r)
def init_class():
    return 'Has been init!'
def scan_dic():
    header_buffer = list()
    R = None
    index = 1
    target_dic = os.getcwd()+'/targetd'
    backup_dic = os.getcwd()+'/backupd'
    files = os.listdir(target_dic)

    for file in files:
        f_n =  target_dic + '/'+file

        f = open(f_n,)
        flag = 0
        while 1:
            line = f.readline()
            if '###' in line:
                flag = flag +1
            if(flag!=2):
                # print(line)
                if 'apiVersion' in line:
                    r = str_to_json(line)
                    R = r
                    # print(r)
                elif(':' in line and flag == 1 and '###' not in line):
                    x = line.split(':')

                    header_buffer.append('\"'+x[0]+'\"'+':'+'\"'+x[1].replace('\n','').strip(' ')+'\"'+',')
                    # print(header_buffer)
                    # header_buffer.append('"')

            if (flag==2):
                break
    r1 = ''.join(header_buffer)
    matchlist = MatchList(1,'test',r1,R)
    print(matchlist.data)
    return matchlist
        # target_f = target_dic+'/'+file
        # backup_f = backup_dic+'/' + repr(index)+'.txt'
        # s= init_class()
        # shutil.move(target_f,backup_f)
        # index = index + 1
scan_dic()



