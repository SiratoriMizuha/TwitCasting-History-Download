# 功能介绍
本脚本为TC台历史记录一键扒源下载脚本，在python2.0的环境下编写，所以需要的模块目前都是2.0的模块
算法简单介绍为普通爬虫以及使用https://dl02.twitcasting.tv/进行下载
算法实现了对有无存档的识别，但带锁的档实在没办法下载，正在直播中的也不会下载
因为TC台才下播的档不会给日期，所以我直接用的当日时间，最后的格式会有点不一样，不过我懒人懒得设计统一了。。。

# 依赖
该脚本主要设计为在linux上运行，需要的模块为

- requests
- BeautifulSoup4

建议直接用pip指令下载即可
懒人复制
```
pip install requests
pip install beautifulsoup4
```
同时需要用到[OneDrive for Business on Bash](https://github.com/0oVicero0/OneDrive)

操作说明参考https://www.moerats.com/archives/697/

顺便因为考虑到脚本下载的视频量应该比较大，可能下到一半服务器容量就满了，所以下载好后是直接上传到OneDrive并删除服务器上的视频文件的

所以使用本脚本前请先务必将上面的OneDrive依赖下好

# 使用方法
本脚本只有两个参数

示例为
`python twitcast_spider.py user_id file`

user_id为要下载的主播的id

例如利香的主页为https://twitcasting.tv/kuroneko_datenn

她的user_id即为kuroneko_datenn

file为你的onedrive保存路径

比如上面录制的利香可以统一保存在record/rika之类的路径里，当然取自己喜欢的路径名字就行
但路径不在服务器上事先创建好的话会报错，不过OneDrive上会自动创建
当前台直接操作时用
`python twitcast_spider.py kuroneko_datenn record/rika`

终端不关闭后台运行时用
`python twitcast_spider.py kuroneko_datenn record/rika > rika.log &`
即可

这里rika.log为日志的名字，也是取自己喜欢的名字就行

如果关闭终端后台运行的话就可以用

`nohup python -u twitcast_spider.py kuroneko_datenn record/rika > rika.log &`

这里如果不加-u参数的话日志会缓冲，导致不能及时显示内容
具体其他后台相关操作可以看[这里](https://blog.csdn.net/weixin_39561473/article/details/89765106)

# 补充
其实本人设计的这个脚本比较粗糙，也没有防错机制，所以如果出了什么毛病还请自己检查一下日志
另外爬虫因为用的是最基本的结构，所以速度上可能不太行，本人试验了一下扒50多页十几个源约用了30多分钟，不过感觉应该没人对这个速度很有需求吧。。。这方面以后找机会改进一下
还有就是扒太多可能又被封ip的风险，如果想多爬的可以用Selenium改进一下，不过我也没被封，先观望下有无改进必要
