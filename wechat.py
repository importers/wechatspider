#coding=utf-8
import requests, re
import time,os,sys

class wechat:
	def __init__(self,openid,ext):
		self.openid=openid
		self.ext=ext
		#self.SNUID='28E1F2B62624930A0000000056ADF82F'
		self.SNUID=self.cookies(self.openid,self.ext)
	def __del__(self,):
		pass
	def weichatget(self,openid,ext,page):
		cookies = {'SNUID':self.SNUID}#只要带着SNUID就可以获取mp.weixin的内容了
		headers = {'Host':'weixin.sogou.com',
					'Referer':'http://weixin.sogou.com/gzh?openid=oIWsFtwbC_RfPo29wSlbi2WbTTF4&ext=p8lVKENENblLmE56fkit_Lgdn9pCUVTZ4-IV1IMNqJ6sx7GaWItqcT8rbV-JBL_Y',
					'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.97 Safari/537.36',
					'X-Requested-With':'XMLHttpRequest'}
		payload = {'openid': openid, 'ext': ext, 'cb': 'sogou.weixin_gzhcb', 'tsn': 0, 'page': page}			
		r = requests.get("http://weixin.sogou.com/gzhjs", params=payload,cookies=cookies,headers=headers)
		return r.text.encode('utf8')
	#获取SNUID
	def cookies(self,openid,ext):
			payload = {'openid': openid, 'ext': ext, 'cb': 'sogou.weixin_gzhcb', 'tsn': 0}
			headers = {'Host':'weixin.sogou.com',
					'Referer':'http://weixin.sogou.com',
					'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.97 Safari/537.36',
					'X-Requested-With':'XMLHttpRequest'}
			r = requests.get("http://weixin.sogou.com/gzhjs", params=payload,headers=headers)

			return r.cookies['SNUID']
	def getdata(self,url):
		cookies = {'SNUID':self.SNUID}#只要带着SNUID就可以获取mp.weixin的内容了
		r = requests.get(url,cookies = cookies)	
		return r.text.encode('utf8')	
	#根据得到的url 获得微信文章并保存
	def geturl(self,data,pagei,file_name):
			reg = r"<title><!\[CDATA\[(.*?)]]><\\/title><url><!\[CDATA\[(.*?)]]><\\/url>.*?<sourcename><!\[CDATA\[(.*?)]]><\\/sourcename>.*?<date><!\[CDATA\[(.*?)]]><\\/date>"
			xi=0
			htmlre = re.compile(reg,re.S)		#获取标题及url
			htmllist = re.findall(htmlre,data) 
			if len(htmllist)<1:return None
			for html in htmllist:
				print '----%s----'%xi
				#公众号名称
				wechat_name = html[2].decode('utf8')
				#微信文章页面地址
				s_url = 'http://weixin.sogou.com%s'%html[1]
				#保存文章页文件名
				htmlname=html[0].decode('utf8')
				#print string 去除标点符号
				string = re.sub("[\s+\.\!\/_,$%^*(+\"\']+|[+——！!，。? ？、~@#￥%【】&*（）]+".decode("utf8"), "".decode("utf8"),htmlname)
				#公众号以时间为文件夹路径
				wechat_date_dir='./%s/%s'% (wechat_name,html[3])
				#创建以时间文件夹
				self.mkdir(wechat_date_dir)
				#文件保存路径
				path_file='%s/%s.html'%(wechat_date_dir,string)
				#保存文件
				tit=open(path_file,'w')
				tit.write(self.getdata(s_url)) 
				tit.close()
				xi+=1
				print "save to %s"%path_file
				time.sleep(1)
	#创建新目录
	def mkdir(self,path):
	    path = path.strip()
	    # 判断路径是否存在
	    # 存在     True
	    # 不存在   False
	    isExists=os.path.exists(path)
	    # 判断结果
	    if not isExists:
	        # 如果不存在则创建目录
	        print u"新建了名字叫做",path,u'的文件夹'
	        # 创建目录操作函数
	        os.makedirs(path)
	        return True
	    else:
	        # 如果目录存在则不创建，并提示目录已存在
	        print u"名为",path,u'的文件夹已经创建成功'
	        return False			
	def run(self):
		file_name=self.openid
		for page in range(11): 			
			self.geturl(self.weichatget(self.openid,self.ext,page),page,file_name)		


			
				