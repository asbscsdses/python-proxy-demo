'''
读取代理文件，打印出每个代理的物理地址
'''
import re,requests,threading

import msvcrt as m
def wait():
	m.getch()
	
def get_lines(fname):
	with open(fname,'r') as f:
		lines=[x.strip() for x in f.readlines()]
		return lines	

def print_proxy_location(proxy_ip_port):
	headers = { 'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)' }
	url = 'http://1212.ip138.com/ic.asp'
	proxy = {'http':'http://{:s}'.format(proxy_ip_port),}
	try:
		r = requests.get(url, headers=headers, proxies=proxy, timeout=10)
		if r.status_code == 200:
			#print('请求成功')
			r.encoding = 'gb2312'
			#print(r.encoding)
			#print()
			reg = re.compile(".+<center>(.+)</center>.+",re.DOTALL)
			print(reg.match(r.text).group(1))
		else:
			print('status_code:{:d}'.format(r.status_code))
	except Exception as e:
		#print('Exception:{:s}'.format(e))
		print('Exception happened with ip {:s}'.format(proxy_ip_port))
	
if __name__=='__main__':
	lines=get_lines('proxies.txt')
	index = 1;
	for line in lines:
		if index%10 == 0:
			print()
			print("Press any key to continue")
			wait()
			print()
		else:
			print_proxy_location(line)
		
		index+=1
			
	print()
	print("Press any key to exit")
	wait()