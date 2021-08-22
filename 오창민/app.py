from typing import Text
import requests
from bs4 import BeautifulSoup
from flask import Blueprint, render_template,flash,redirect,url_for
from flask import current_app as current_app

 

req = requests.get('https://www.google.com/search?q=%EA%B5%B0%ED%8F%AC%EC%8B%9C+%EB%8B%B9%EB%8F%99++%EC%9D%BC%EC%A3%BC%EC%9D%BC+%EB%82%A0%EC%94%A8&rlz=1C1CHBD_koKR942KR942&ei=i0TwYIStCMeGoASQ_JCYCg&oq=%EA%B5%B0%ED%8F%AC%EC%8B%9C+%EB%8B%B9%EB%8F%99++%EC%9D%BC%EC%A3%BC%EC%9D%BC+%EB%82%A0%EC%94%A8&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEM0COgUIABCwAzoJCAAQsAMQCBAeOgcIABBGEIACOgYIABAHEB46CQgAEA0QRhCAAjoICAAQCBANEB5KBAhBGAFQrRRYsyFg6CJoA3AAeACAAXWIAaMKkgEEMC4xMpgBAKABAaoBB2d3cy13aXrIAQLAAQE&sclient=gws-wiz&ved=0ahUKEwjEnpCPo-XxAhVHA4gKHRA-BKMQ4dUDCA4&uact=5')
raw = req.text
soup = BeautifulSoup(raw, 'html.parser')
infos = soup.select('div.ZINbbc.xpd.O9g5cc.uUPGi > div.kCrYT > span')
위치 = ""
for i in infos:
    위치 = 위치 +(i.text)

infos = soup.select("div.kvKEAb")
정보 = " "
for i in infos[:1]:
    정보 = 정보 +(i.text)
a = "".join(정보)[:-11]
b = 위치 + a
def senddata():
    return render_template('a.html',data=b)




