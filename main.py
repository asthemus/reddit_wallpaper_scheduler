bot_secret = 'XXXX'
bot_username = 'XXXX'
bot_password = 'XXXX'
bot_client_ID = 'XXXX'

import requests, csv, time
import praw
import cv2
import urllib
import os
import shutil

loc = '/home/asthemus/Pictures/Wallpapers/'
for filename in os.listdir(loc):
    file_path = os.path.join(loc, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (file_path, e))

#os.chdir('/home/asthemus/Pictures/Wallpapers/')
#os.system('pwd')

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
	
	with open(loc+'img_'+str(idx)+ext,'wb') as handler:
		handler.write(img_data)

reddit = praw.Reddit(user_agent='XXXX',
                     client_id=bot_client_ID, client_secret=bot_secret,
                     username=bot_username, password=bot_password)

print("Praw connected")
print("Connecting Subreddit")
sub = reddit.subreddit("wallpapers")
count = 0
img_arr = []
print("getting subreddit")

print("scrapping image links")
for submission in sub.top('week'):
	url = str(submission.url)
	if(('i.redd.it' in url) or ('i.imgur.com' in url)):
		if(check_dim(url)):
			img_arr.append(url)
			count+=1
	if(count==100):
		break

print("Image links recieved")

for idx,url in enumerate(img_arr):
	download_img(idx,url)
	print("downloaded  ---->"+url)		

