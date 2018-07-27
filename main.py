import get_url_info as gui
import re,threading,os

url_list_int=[x for x in range(1,1001)]
sw_path='sw' #古诗存储路径

def get_sw(sw_url):
	sw_context=gui.get_link(sw_url)
	sw_re=r'(?<=<div class=\"contson\" id=\")\w+">(.*?)(?=</div>)'
	sw_msg=gui.find_re_info(sw_context.text,re.compile(sw_re,re.S))
	sw_title_re=r'(?<=<a style="font-size:18px; line-height:22px; height:22px;" href="https://so\.gushiwen\.org/shiwenv_)\w+\.aspx" target="_blank"><b>(.*?)(?=</b></a></p>)'
	sw_title_msg=gui.find_re_info(sw_context.text,re.compile(sw_title_re,re.S))
	sw_zz_re=r'(?<=</span><a href="https://so\.gushiwen\.org/search\.aspx)\?value=.*?">(.*?)(?=</a></p>)'
	sw_zz_msg=gui.find_re_info(sw_context.text,re.compile(sw_zz_re,re.S))
	sw_zz_cd_re=r'(?<=<a href="/shiwen/default\.aspx\?cstr=).*?">(.*?)(?=</a><span>)'
	sw_zz_cd_msg=gui.find_re_info(sw_context.text,re.compile(sw_zz_cd_re,re.S))
	return [sw_title_msg,sw_zz_cd_msg,sw_zz_msg,sw_msg]

def write_sw(sw_url_msg,path):
	if not os.path.exists(path):
		os.makedirs(path)
	for i in range(len(sw_url_msg[0])):
		file=path+'/'+sw_url_msg[0][i].replace('/','or').replace('?','？').replace('：',':').replace('"','')+'.txt'
		gui.write_file_w(file,sw_url_msg[0][i]+'\n')
		zz=sw_url_msg[1][i]+':'+sw_url_msg[2][i]
		gui.write_file_a(file,zz)
		file_msg=re.sub(r'<span style="font-family:SimSun;">.*</span>','',sw_url_msg[3][i])
		gui.write_file_a(file,file_msg.replace('<br>','\n').replace('<p>','')
			.replace('</p>','').replace('<br />','').replace('<strong>','').replace('</strong>','')
			.replace('<span style="font-family:SimSun;">','').replace('</span>','').replace('<br/>','')+'\n\n')

def main(t_i):
	names = locals()
	for i in range(1,t_i):
		names['t%s' % i]=threading.Thread(target=t_start)
		names['t%s' % i].setDaemon(True)
		names['t%s' % i].start()
		names['t%s' % i].join()

def t_start():
	while True:
		if len(url_list_int) ==0:
			break
		page_id=url_list_int.pop()
		sw_url='https://www.gushiwen.org/shiwen/default_0A0A'+str(page_id)+'.aspx'
		print(sw_url)
		sw_url_msg=get_sw(sw_url)
		write_sw(sw_url_msg,sw_path)

if __name__ == '__main__':
	main(5)
