#coding=utf-8
# import re
import json,requests
import sys

attachinfo=[]
#获取QQ空间内容
def getcontent(res_attach):
	cookies={'ptisp':'ctc', 
		'ptcz':'c891330bc26d9c0114441e63672a1ce1a4bcc0d8a47c65727285faa7277bea66', 
		'pt2gguin':'o1229323202', 
		'uin':'o1229323202', 
		'skey':'@ho1eufRw3', 
		'p_uin':'o1229323202', 
		'p_skey':'80w8gQEZCjM4oreuAhRUmglvj9vvlQZU41roH2Upbb4_', 
		'pt4_token':'W4GZ0fLn8CCG9ULY759vwdYoFWAovPclrpTTPVE2bW8_', 
		'pgv_pvid':'2115985090', 
		'pgv_info':'s4482467556',
		'ssid':'s4482467556'}
	payload = {'g_tk':'305487353','res_type':0,
		'res_attach':res_attach,
		'refresh_type':2,
		'format':'json'}
	headers = {'Host':'m.qzone.com',
			'Referer':'http://m.qzone.com/',
			'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.97 Safari/537.36',
			'X-Requested-With':'XMLHttpRequest'}
	r = requests.get("http://m.qzone.com/get_feeds",params=payload,cookies=cookies)
	return r.text
	

attachinfo.append(sys.argv[1])
#注意此处的为下一页的 res_attach 
print '\r\n --start---->'
#attachinfo.append(xx['data']['attachinfo'])
while len(attachinfo)>=1: 
	string = getcontent(attachinfo.pop())
	#info=get_data(string)
	#attachinfo.append(info)
	#解析json数据
	# path=sys.argv[1]
	# f=open(path)
	# data=f.read()
	# loads=data.decode('gbk').encode('utf8')	
def get_data(strings):
	xx=json.loads(strings.encode('utf8'))
	return xx['code']['attachinfo']	
	