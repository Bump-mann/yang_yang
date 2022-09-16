import requests


headers = {
    'Host'        : 'cat-match.easygame2021.com',
    'Connection'  : 'keep-alive',
    't'           : 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTQzMzMxNjcsIm5iZiI6MTY2MzIzMDk2NywiaWF0IjoxNjYzMjI5MTY3LCJqdGkiOiJDTTpjYXRfbWF0Y2g6bHQxMjM0NTYiLCJvcGVuX2lkIjoiIiwidWlkIjo4Nzc4OTg2OSwiZGVidWciOiIiLCJsYW5nIjoiIn0.qPMhKSGMikH-T3zIzeIYa343pFD0jpoWl9mIDAljL4U',
    'content-type': 'application/json',
    'User-Agent'  : 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.26(0x18001a34) NetType/WIFI Language/zh_CN',
    'Referer'     : 'https://servicewechat.com/wx141bfb9b73c970a9/15/page-frame.html',
}

params = {
    'rank_score': '1',
    'rank_state': '1',
    'rank_time' : '40',#通过时间
    'rank_role' : '1',
    'skin'      : '1',
}
#通关次数
num = 100

for i in range(num):
    response = requests.get('https://cat-match.easygame2021.com/sheep/v1/game/game_over', params=params, headers=headers)
    print(response.text)
