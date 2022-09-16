# yang_yang
热门微信小程序羊了个羊通关次数刷取代码




以下是示例代码，其中 **t参数** 需要换成自己的，获取方法为，通过抓包获取

GitHub：

```python
import requests
import time


headers = {
    'Host'        : 'cat-match.easygame2021.com',
    'Connection'  : 'keep-alive',
    't'           : '',#换成你自己的
    'content-type': 'application/json',
    'User-Agent'  : 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.26(0x18001a34) NetType/WIFI Language/zh_CN',
    'Referer'     : 'https://servicewechat.com/wx141bfb9b73c970a9/15/page-frame.html',
}

params = {
    'rank_score': '1',
    'rank_state': '1',
    'rank_time' : '40',#通关时间
    'rank_role' : '1',
    'skin'      : '1',
}
#通关次数
num = 100

for i in range(num):
    response = requests.get('https://cat-match.easygame2021.com/sheep/v1/game/game_over', params=params, headers=headers)
    print(response.text)
```
t参数获取方式：
使用Fiddler对其抓包获取，微信版本建议使用3.6
如果不会抓包可以参考下： [最新微信小程序抓包方法](https://blog.csdn.net/m0_64910183/article/details/126534293)


抓到包后搜索关键字： e2021.c
![在这里插入图片描述](https://img-blog.csdnimg.cn/4b2d158a7357447dbcee709adb2141ab.png)
找到两个，然后选择查看第一个的headers信息
![在这里插入图片描述](https://img-blog.csdnimg.cn/f62b1457c47f463f8631917770e6a9af.png)
复制下来t的参数，带入到代码中的t，修改下num、rank_time，运行就可以啦
运行效果如下
![在这里插入图片描述](https://img-blog.csdnimg.cn/eb56918a07cf41c19e987f262e1ac209.png)



如果实在不会搞的话，可以加下q群：**949504676**  里面有很多热心肠的大佬哦！
