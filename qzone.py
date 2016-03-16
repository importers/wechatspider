#coding=utf-8
# import re
import json,requests
import sys

#获取QQ空间内容
def getcontent():
	cookies={'pgv_pvid':'2115985090', 
	'pgv_info':'s2237470552',
	'ssid':'s2237470552', 
	'ptisp':'ctc', 
	'ptcz':'c891330bc26d9c0114441e63672a1ce1a4bcc0d8a47c65727285faa7277bea66', 
	'cache_hit_test_600':'1', 
	'cache_hit_test_3600':'1', 
	'cache_hit_test_31536000':'1', 
	'pt2gguin':'o1229323202', 
	'uin':'o1229323202', 
	'skey':'@OxwTyeJ64', 
	'p_uin':'o1229323202', 
	'p_skey':'2rUX5zszkW*YNiY8Mj42VH1WnE47iPY-o-I5sV6dpeo_', 
	'pt4_token':'L8WJS5GVWeZfNtT2JkHzDAmsWKMyssFAUedonoqSAd8_', 
	'g_ut':'3', 
	'network_type':'3'}

	payload = {'g_tk':'390100575','res_type':0,
		'res_attach':'att=back%5Fserver%5Finfo%3Dbasetime%253D1458093793%2526pagenum%253D3%2526dayvalue%253D0%2526getadvlast%253D0%2526hasgetadv%253D%2526lastentertime%253D1458122976%2526LastAdvPos%253D0%26lastrefreshtime%3D1458137435%26lastseparatortime%3D0%26loadcount%3D1&tl=1458093793',
		'refresh_type':2,
		'format':'json'}
	headers = {'Host':'m.qzone.com',
			'Referer':'http://m.qzone.com/',
			'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.97 Safari/537.36',
			'X-Requested-With':'XMLHttpRequest'}
	r = requests.get("http://m.qzone.com/get_feeds",params=payload,cookies=cookies)
	return r.text
print u'--------解析---------'
print r.url
#print string
# def analyze(strings):
# 	xx=json.loads(strings.encode('utf8'))
# 	return xx['data']['attachinfo']
# #analyze(string)
xx=json.loads(string.encode('utf8'))
# #注意此处的为下一页的 res_attach 
print xx['data']['attachinfo'] 
while len(attachinfo)>=1: 
	string = getcontent(attachinfo.pop())
# def analyze(string):
# 	#解析json数据
# 	# path=sys.argv[1]
# 	# f=open(path)
# 	# data=f.read()
# 	# loads=data.decode('gbk').encode('utf8')
# 	xx=json.loads(string)
# 	print xx['code']
