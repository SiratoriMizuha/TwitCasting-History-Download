import re
import requests
from lxml import html
from bs4 import BeautifulSoup
import os
import urllib2,urllib
import sys
import time


def main(url_sub,file_dir):
    url_base='https://twitcasting.tv/'
    url=url_base+url_sub+"/show"
    print(url)



    def get_html(url):
        html = urllib2.urlopen(url).read().decode('utf-8')
        return html


    def parse_html(html):
        soup = BeautifulSoup(html, features='lxml')
        now_page=soup.find('a',{'href':re.compile("/"+url_sub+"/show/.+?"),'class':"selected"}).get_text()
        print (now_page)
        video_test(soup)
        paging=soup.find_all('a',{'href':re.compile("\A/"+url_sub+"/show/.+?")})
        for all_page in paging:
            if int(all_page.get_text())==int(now_page)+1:
                next_page=all_page
                next_page_url=url_base+next_page.get('href')
                parse_html(get_html(next_page_url))


    def video_test(soup):
        video_page=soup.find_all('a',{'class':"tw-movie-thumbnail",'href':re.compile("\A/"+url_sub+"/movie/.+?")})
        for video in video_page:
            video_url=url_base+video.get('href')
            print(video_url)
            video_html=get_html(video_url)
            soup1 = BeautifulSoup(video_html, features='lxml')
            is_archive=soup1.find('video',{"data-movie-url":re.compile(".+?")})
            # print (is_archive)
            if is_archive:
                video_download(video.get('href'))

    def video_download(url):
        url_split=re.split(r"[/]",url)
        user_id=url_split[1]
        video_id=url_split[3]
        dlurl="https://dl02.twitcasting.tv/"+user_id+"/download/"+video_id
        soup=BeautifulSoup(get_html("https://twitcasting.tv"+url), features='lxml')
        date_all=str(soup.find_all("span",{"class":"tw-player-meta__status_item"}))
        pattern=r'var d = new Date\(Date.parse\(\"(?P<date>.+)\"\)\)'
        match=re.search(pattern,date_all)
        if match:
            date=match.group("date")
            date=re.sub(r'[,\s]','_',date)
            date=re.sub(':','',date)
        else:
            date=time.strftime("%Y%m%d",time.localtime())
        file_name=user_id+'_'+video_id+'_'+date+'.mp4'
        path = file_dir
        dest_dir = os.path.join(path, file_name)
        try:
            urllib.urlretrieve(dlurl,dest_dir)
        except:
            print('\tError retrieving the URL:',dest_dir)
        print(file_name)
        onedrive(file_name)

    def onedrive(file_name):
        onedrive_send="onedrive -s -f "+file_dir+" "+file_dir+"/"+file_name
        os.popen(onedrive_send)
        os.popen("rm -f "+file_dir+"/"+file_name)

    parse_html(get_html(url))



main(sys.argv[1], sys.argv[2])