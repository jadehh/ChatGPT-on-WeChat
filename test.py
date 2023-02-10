#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File     : test.py
# @Author   : jade
# @Date     : 2023/2/10 17:00
# @Email    : jadehh@1ive.com
# @Software : Samples
# @Desc     :
from wxauto import *


def login_wechat():
    # 获取当前微信客户端
    wx = WeChat()

    # # 向某人发送消息（以`文件传输助手`为例）
    # msg = '你好~'
    # who = 'Jade'
    # wx.ChatWith(who)  # 打开`文件传输助手`聊天窗口
    # wx.SendMsg(msg)  # 向`文件传输助手`发送消息：你好~
    # 输出当前聊天窗口聊天消息
    wx.GetSessionList()
    msgs = wx.GetAllMessage
    for msg in msgs:
        print('%s : %s' % (msg[0], msg[1]))
    ## 获取更多聊天记录
    while True:
        wx.LoadMoreMessage()
        msgs = wx.GetAllMessage
        for msg in msgs:
            print('%s : %s' % (msg[0], msg[1]))


if __name__ == '__main__':
    login_wechat()