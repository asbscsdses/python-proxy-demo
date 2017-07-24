'''
读取代理文本文件，每100条数据打印一次
'''
from pyecho import echo
import msvcrt as m
def wait():
	m.getch()
	
def get_lines(fname):
	with open(fname,'r') as f:
		lines=[x.strip() for x in f.readlines()]
		return lines

if __name__ == '__main__':
	lines=get_lines('proxies.txt')
	index = 1;
	for line in lines:
		if index%100 == 0:
			print()
			print("Press any key to continue")
			wait()
			print()
		else:
			print(line)
		
		index+=1
	
	print()
	print('{:d} records is processed'.format(index-1))
	print()
	print("Press any key to exit")
	wait()