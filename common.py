#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import requests
import csv
import pandas as pd

class Common():
    """
    @brief : Pythonでよく使用する関数を集めたクラス
    @note  : 
    """
    line_notify_token = ''
    discord_webhook_url = ''
    discord_username = ''
    slack_webhook_url = ''
    slack_username = ''
    
    def __init__(self):
        print("Commonクラスをインスタンス化")

    def get_csv_val(self, file_name, row, col):
        """
        @brief : ファイル名と行列を指定してCSVの値を取得
        @note  : CSVファイルの1行目はカラム名データとなるため、2行目からのデータが取得可能なことに注意
                  始め（2行目）のデータ→(行:0,列:0)
        """        
        if os.path.exists(file_name):
            csv_input = pd.read_csv(file_name)
            return csv_input.values[row, col]
        else:
            print(file_name + " が存在しません。")
 
    def get_csv_val_by_key(self, file_name, name):
        """
        @brief : ファイル名とkeyを指定してCSVの値を取得
        @note  : ファイルに格納されているデータは下記のような形式
                  name1, key1
                  name2, key2
                  ・
                  ・
        """
        key_dict = {}
        with open(file_name, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                key_dict[row[0]] = row[1]
                #print(key_dict)
        return key_dict[name]

    # ----- LINE, DISCORD, SLACK にメッセージを送るための初期設定 関連----
    def set_line(self, token):
        self.line_notify_token = token

    def set_discord(self, url, username):
        self.discord_webhook_url = url
        self.discord_username = username
    
    def set_slack(self, url, username):
        self.slack_webhook_url = url
        self.slack_username = username        

    # ----- Notify（メッセージを送る） 関連-----
    def send_message(self, text) :
        try:
            self.__line(text)
        except:
            pass
        try:
            self.__discord(text)
        except:
            pass
        try:
            self.__slack(text)
        except:
            pass
        
    def __line(self, message):
        if len(self.line_notify_token) > 0:
            requests.post('https://notify-api.line.me/api/notify', headers={'Authorization': 'Bearer ' + self.line_notify_token}, data={'message': '\n' + message})

    def __discord(self, message):
        if len(self.discord_webhook_url) > 0:
            requests.post(self.discord_webhook_url, data={'username': self.discord_username, 'content': message})

    def __slack(self, message):
        if len(self.slack_webhook_url) > 0:
            requests.post(self.slack_webhook_url, data=json.dumps({'username': self.slack_username, 'text':message}))

    


# In[2]:


# ---- For Debug ----
#common = Common()
#token = common.get_csv_val_by_key("../keys.csv", "line_token")
#print(token)
#common.set_line(token)
#common.send_message("test")

