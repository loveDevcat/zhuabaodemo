# coding=utf-8
import os
import sys

import requests

# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

print("开始执行")
headers = {
    "Host": "ssl.kohsocialapp.qq.com:10001",
    "Accept": "*/*",
    "X-Client-Proto": "https",
    "Accept-Language": "zh-cn",
    "Accept-Encoding": "br,gzip,deflate",
    "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
    "Content-Length": "1791",
    "User-Agent": "smoba/2019101809 CFNetwork/978.0.7 Darwin/18.6.0",
    "Connection": "keep-alive",
    "noencrypt": "1",
    "Accept-Encrypt": "",
    "Cookie": "_qz_referrer=qzs.qq.com;pgv_pvid=5457054890;pgv_pvi=3969268736;eas_sid=u1I5h738S2D27572c8D8M1K0y0"
}
headers1 = {
        "Host":"ssl.kohsocialapp.qq.com:10001",
        "Content-Type":"application/x-www-form-urlencoded",
        "Accept-Encoding":"br, gzip, deflate",
        "Cookie":"pgv_pvid=5457054890;pgv_pvi=3969268736;eas_sid=u1I5h738S2D27572c8D8M1K0y0",
        "Connection":"keep-alive",
"Accept": "*/*",
"User-Agent": "smoba/3.46.202 (iPhone; iOS 12.3.1; Scale/2.00)",
"Accept-Language": "zh-Hans-CN;q=1, zh-Hant-CN;q=0.9, ko-KR;q=0.8",
"noencrypt": "1",
"Content-Length": "697"

}
data = {"toServerID":"2055",
        "modulename":"battledetail",
        "roleLevel":"30",
        "serverId":"2055",
        "msdkEncodeParam":"E8547FE3B3CA15E2DCDC2D2FFB2C8ECD6EFF6F4A0FB3AB8F9E1594E298AD018E99D38A3C86D3BC6267553C99D9EC5E5404FAEA2296D5C5C80FEF7A76C5A22AB28C07CBB3F42F0429DBC6EE5ED7A096153E5DD2F2DC5910E75A9CD44FF2B07F99A49342AC32F3F5AB0399336DE18741EFE8E1BBCD3BB9589C8AD7EBFC85D42A18BC89E7C80BB89318469A2DE151F389EDB52ACA3BF9801A43B83B1A5A48882857F9A1505CD45CFE7B4BF40B431A82F59D",
        "qi":"1",
        "uniqueRoleId":"106588992",
        "areId":"2",
        "roleId":"1961066319",
        "toAreaID":"2",
        "acntCamp":"1",
        "source":"smoba_zhushou",
        "userId":"90873130",
        "platid":"0",
        "roleName":"干的漂亮",
        "toAppRoleId":"106588992",
        "gameOpenid":"8AD687FC68C4650858AA1A6CC166AAF6",
        "JLRoutePattern":"/hippy",
        "pvpType":"5",
        "role":"干的漂亮",
        "zn":"苹果手Q45区",
        "appid":"1105200115",
        "gameSeq":"1581393559",
        "isOpenBattleAssist":"0",
        "uin":"EE865F5146EA7AE701DA87B099739DA9",
        "openid":"EE865F5146EA7AE701DA87B099739DA9",
        "isOpenBattlePro":"0",
        "gameSvrId":"299287",
        "appVersionName":"3.46.202",
        "battleType":"16",
        "gameId":"20001",
        "serverName":"手Q45区",
        "toGameOpenId":"8AD687FC68C4650858AA1A6CC166AAF6",
        "encode":"2",
        "areaName":"苹果",
        "sig":"37b75022d509427eda4e8f215ccce12c",
        "appVersion":"2019191809",
        "isSimulator":"false",
        "toOpenId":"8AD687FC68C4650858AA1A6CC166AAF6",
        "toUin":"EE865F5146EA7AE701DA87B099739DA",
        "nickname":"Plankton",
        "version":"3.1.96i",
        "JLRouteURL":"[object NSURL]",
        "toGameRoleId":"1951066319",
        "relaySvrId":"588120322",
        "timestamp":"1582163449920",
        "wi":"1",
        "env":"https://ssl.kohsocialapp.qq.com:10001/",
        "appOpenId":"EE865F5146EA7AE701DA87B099739DA9",
        "algorithm":"v2",
        "JLRouteScheme":"JLRoutesGlobalRoutesScheme",
        "z":"2055",
        "roleJob":"最强王者",
        "filterType":"0",
        "__instanceName__":"battledetail",
        "__instanceId__":"10",
        "gameOpenId":"8AD687FC68C4650858AA1A6CC166AAF6",
        "formType":"1",
        "msdkToken":"j5FW8cGN",
        }
d1 = {"apiVersion":"3","cChannelId":"0","cClientVersionCode":"2019101809","cClientVersionName":"3.46.202","cCurrentGameId":"20001","cDeviceCPU":"ARM64","cDeviceId":"eb51be8d777cf88fe561c08eb6a9bb9e3fde35e8","cDeviceIdfa":"0AECED4C-0439-44FB-9894-0417A68EA543","cDeviceMem":"2086879232","cDeviceModel":"iPhone","cDeviceNet":"WiFi","cDeviceSP":"中国电信","cDeviceScreenHeight":"667","cDeviceScreenWidth":"375","cGameId":"20001","cGzip":"1","cRand":"1582285217338","cSystem":"ios","cSystemVersionCode":"12.3.1","cSystemVersionName":"iOS","friendUserId":"358403327","gameAreaId":"2","gameId":"20001","gameOpenId":"8AD687FC68C4650858AA1A6CC166AAF6","gameRoleId":"106588992","gameServerId":"2055","gameUserSex":"0","isMi":"0","lastTime":"0","option":"0","roleId":"118026253","token":"UHcG2DJF","userId":"90873130"
}

h3 = {"Host":"ssl.kohsocialapp.qq.com","Content-Type":"application/x-www-form-urlencoded","Accept-Encoding":"br, gzip, deflate","Cookie":"pgv_pvid=5457054890; pgv_pvi=3969268736; eas_sid=u1I5h738S2D27572c8D8M1K0y0","Connection":"keep-alive","Accept":"*/*","User-Agent":"smoba/3.46.202 (iPhone; iOS 12.3.1; Scale/2.00)","Accept-Language":"zh-Hans-CN;q=1, zh-Hant-CN;q=0.9, ko-KR;q=0.8","noencrypt":"1","Content-Length":"697" }
d3 = {"apiVersion":"3","cChannelId":"0","cClientVersionCode":"2019101809","cClientVersionName":"3.46.202","cCurrentGameId":"20001","cDeviceCPU":"ARM64","cDeviceId":"eb51be8d777cf88fe561c08eb6a9bb9e3fde35e8","cDeviceIdfa":"0AECED4C-0439-44FB-9894-0417A68EA543","cDeviceMem":"2086879232","cDeviceModel":"iPhone","cDeviceNet":"WiFi","cDeviceSP":"%E4%B8%AD%E5%9B%BD%E7%94%B5%E4%BF%A1","cDeviceScreenHeight":"667","cDeviceScreenWidth":"375","cGameId":"20001","cGzip":"1","cRand":"1582285217338","cSystem":"ios","cSystemVersionCode":"12.3.1","cSystemVersionName":"iOS","friendUserId":"358403327","gameAreaId":"2","gameId":"20001","gameOpenId":"8AD687FC68C4650858AA1A6CC166AAF6","gameRoleId":"106588992","gameServerId":"2055","gameUserSex":"0","isMI":"0","lastTime":"0","option":"0","roleId":"118026253","token":"UHcG2DJF","userId":"90873130"
}

h10 = {"Host": "ssl.kohsocialapp.qq.com:10001", "Content-Type": "application/x-www-form-urlencoded",
      "Accept-Encoding": "br,gzip,deflate",
      "Cookie": "pgv_pvid=5457054890;pgv_pvi=3969268736;eas_sid=u1I5h738S2D27572c8D8M1K0y0", "Connection": "keep-alive",
      "Accept": "*/*", "User-Agent": "smoba/3.46.202(iPhone;iOS12.3.1;Scale/2.00)",
      "Accept-Language": "zh-Hans-CN;q=1,zh-Hant-CN;q=0.9,ko-KR;q=0.8", "noencrypt": "1", "Content-Length": "696"}
d10 = {"apiVersion":"3","cChannelId":"0","cClientVersionCode":"2019101809","cClientVersionName":"3.46.202","cCurrentGameId":"20001","cDeviceCPU":"ARM64","cDeviceId":"eb51be8d777cf88fe561c08eb6a9bb9e3fde35e8","cDeviceIdfa":"0AECED4C-0439-44FB-9894-0417A68EA543","cDeviceMem":"2086879232","cDeviceModel":"iPhone","cDeviceNet":"WiFi","cDeviceSP":"%E4%B8%AD%E5%9B%BD%E7%94%B5%E4%BF%A1","cDeviceScreenHeight":"667","cDeviceScreenWidth":"375","cGameId":"20001","cGzip":"1","cRand":"1582371965712","cSystem":"ios","cSystemVersionCode":"12.3.1","cSystemVersionName":"iOS","friendUserId":"90873130","gameAreaId":"2","gameId":"20001","gameOpenId":"8AD687FC68C4650858AA1A6CC166AAF6","gameRoleId":"106588992","gameServerId":"2055","gameUserSex":"0","isMI":"0","lastTime":"0","option":"0","roleId":"106588992","token":"3dkw46eN","userId":"90873130"}

response = requests.post("https://ssl.kohsocialapp.qq.com:10001/play/getmatchlist", headers=h10,data=d10 )
print(1)
print(response)
print(response.text)

print('test')
