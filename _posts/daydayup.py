#coding:utf-8
import requests,json,sys


num=172 #需要点赞或者踩的组编号，可以通过网页链接得到
UP=1    #1设置为点赞,-1设置为踩
times=100 #点赞或者踩的次数





do_up='http://me.sjtu.edu.cn/bysj/active/do_up.html'
post_data={'art_id':num}

down_cookie='80%2C'+num

if(UP=='1'):
    #print('UP')
    cookies={}
    #cookies={'click_up':'80'};
elif(UP=='-1'):
    cookies={'click_up':down_cookie};


for i in range(0,times):
    try:
        response=requests.post(do_up,post_data,cookies=cookies)
    except Exception as e:
        continue;
print('finished:',times)
