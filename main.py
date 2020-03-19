bot_secret = 'XXXX'
bot_username = 'XXXX'
bot_password = 'XXXX'
bot_client_ID = 'XXXX'

import requests, csv, time
import praw
import cv2
import urllib
import os

os.chdir('/home/asthemus/Pictures/Wallpapers/')
os.system('pwd')

def check_dim(url):
	return True

def download_img(idx,url):
	if('.png' in url):
		ext = '.png'
	elif('.jpg' in url):
		ext = '.jpg'
	elif('.jpeg' in url):
		ext = '.jpeg'
	else:
		return 
	img_data = requests.get(url).content
	
	with open('img_'+str(idx)+ext,'wb') as handler:
		handler.write(img_data)

reddit = praw.Reddit(user_agent='XXXX',
                     client_id=bot_client_ID, client_secret=bot_secret,
                     username=bot_username, password=bot_password)

sub = reddit.subreddit("wallpapers")
count = 0
img_arr = []

for submission in sub.top('week'):
	url = str(submission.url)
	if(('i.redd.it' in url) or ('i.imgur.com' in url)):
		if(check_dim(url)):
			img_arr.append(url)
			count+=1
	if(count==10):
		break
print(img_arr)

for idx,url in enumerate(img_arr):
	download_img(idx,url)		

