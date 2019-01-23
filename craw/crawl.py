# coding=utf-8
import requests
from lxml import html
LOGIN_URL='https://github.com/login'
SESSION_URL='https://github.com/session'
s=requests.session()
r=s.get(LOGIN_URL)
tree=html.fromstring(r.text)
el=tree.xpath('//input[@name="authenticity_token"]')[0]
authenticity_token=el.attrib['value']
data={
    'commit': 'Sign in',
    'utf8': '✓',
    'authenticity_token':authenticity_token ,
    'login': 'skliucong@gmail.com',
    'password': 'liucong7956'
}
r=s.post(SESSION_URL,data=data)