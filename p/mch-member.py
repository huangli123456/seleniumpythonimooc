#coding=utf-8
#!/usr/bin/env python
import json
import requests


def mch_login(session,url):
    method = "post"
    headers =  {'Content-Type': 'application/json'}
    url = url + "/auth/login.json"
    data = {"reg":"1",
            "password":"Ab123456",
            "username":"gcs1"}
    re = session.post(url=url, data=json.dumps(data), headers=headers)
    re_text = json.loads(re.text)
   # print(re_text)
    return session

"""
1、获取会员信息

def member_list(session,url):
    method = "get"
    headers = {"Content-Type":"application/json"}
    url = url + "/mlpartner/member.json"
    data = { "member_id" = " "}
    re = session.get(url=url,data=json.dumps(data),headers=headers)
    re_text = json.loads(re.text)
    print(re_text)

"""
#2、自定义上级选择上级（就读推客列表）
"""
def guider_list(session,url):
    method = "get"
    headers = {"Content-Type":"application/json"}
    url = url +"/guider.json?column=created_at&created_at=&direction=desc&level=&limit=10&mobile=&nickname=&offset=0&status=all&title="
    data = {"mobile":14773616489}
    re = session.get(url=url,data=json.dumps(data),headers=headers)
    re_text = json.loads(re.text)
    print(re_text)
"""
def shouyi(session,url):
    method = "post"
    headers = {"Content-Type":"application/json"}
    url = url +"/mlpartner/get_model.json"
    data = {"":""}
    re = session.post(url=url,data=json.dumps(data),headers=headers)
    re_text = json.dumps(re.text)

    print(re.text)



if __name__ == "__main__":
    url = "http://mch.weiba456.com"
    session = requests.session()
    mch_login(session,url)
    shouyi(session,url)




