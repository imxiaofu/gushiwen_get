import requests
import re

headers={
	'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'
}

def get_link(url):
	context=requests.get(url,headers=headers)
	return context

def find_re_info(context,compile):
	infos=compile.findall(context)
	return infos

def write_file_w(file,lines):
	fp=open(file,'w+',encoding='UTF-8')
	fp.write(lines)
	fp.close()

def write_file_a(file,lines):
	fp=open(file,'a+',encoding='UTF-8')
	fp.write(lines)
	fp.close()
