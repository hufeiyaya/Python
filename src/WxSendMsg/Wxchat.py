#coding=utf-8
import itchat
import time
print('扫描二维码')
itchat.auto_login(hotReload=True)
boom_remark_name = input('输入目标备注:')
message = input('输入消息内容')
boom_obj = itchat.search_friends(remarkName=boom_remark_name)[0]['UserName']

while True: 
    time.sleep(0.5)
    print('发送完成！')
    itchat.send_msg(msg=message, toUserName=boom_obj)