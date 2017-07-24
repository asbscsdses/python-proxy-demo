'''
读取代理文件，打印出每个代理的物理地址
'''
import re,requests,threading

import msvcrt as m
def wait():
	m.getch()
	
if __name__=='__main__':
	
	headers = { 'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)' }
	url = 'http://1212.ip138.com/ic.asp'
	proxy = {'http':'http://120.77.255.133:8088',}
	try:
		r = requests.get(url, headers=headers, proxies=proxy, timeout=10)
		if r.status_code == 200:
			print('请求成功')
			r.encoding = 'gb2312'
			#print(r.encoding)
			print()
			reg = re.compile(".+<center>(.+)</center>.+",re.DOTALL)
			print(reg.match(r.text).group(1))
		else:
			print('status_code:{:d}'.format(r.status_code))
	except Exception as e:
		print('Exception:{:s}'.format(e))
		
	print()
	print("Press any key to exit")
	wait()
	