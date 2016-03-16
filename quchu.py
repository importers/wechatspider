#coding=utf-8
# import re
import json,requests
import sys
#解析json数据
# path=sys.argv[1]
# f=open(path)
# data=f.read()
# loads=data.decode('gbk').encode('utf8')
# xx=json.loads(loads)
#获取QQ空间内容
cookies={'cookies':{'ptisp':'ctc', 
	'ptcz':'c891330bc26d9c0114441e63672a1ce1a4bcc0d8a47c65727285faa7277bea66', 
	'pt2gguin':'o1229323202', 
	'uin':'o1229323202', 
	'skey':'@ho1eufRw3', 
	'p_uin':'o1229323202', 
	'p_skey':'80w8gQEZCjM4oreuAhRUmglvj9vvlQZU41roH2Upbb4_', 
	'pt4_token':'W4GZ0fLn8CCG9ULY759vwdYoFWAovPclrpTTPVE2bW8_', 
	'pgv_pvid':'2115985090', 
	'pgv_info':'s4482467556',
	'ssid':'s4482467556', 
	'g_ut':3, 
	'network_type':3}}
payload = {'g_tk':'305487353','res_type':0,
	'res_attach':'att=back%5Fserver%5Finfo%3Dbase\time%253D1458007128%2526pagenum%253D3%2526dayvalue%253D0%2526getadvlast%253D0%2526hasgetadv%253D%2526lastentertime%253D1458048259%2526LastAdvPos%253D0%2526recomed%253D1963750026%5F311%5F0%5F8a720c75c110e856432b0400%26lastrefreshtime%3D1458049966%26lastseparatortime%3D0%26loadcount%3D1&tl=1458007128',
	'refresh_type':2,
	'format':'json'}
headers = {'Host':'m.qzone.com',
		'Referer':'http://m.qzone.com/',
		'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.97 Safari/537.36',
		'X-Requested-With':'XMLHttpRequest'}
r = requests.get("http://m.qzone.com/get_feeds", params=payload,headers=headers,cookies=cookies)
print r.content