# youku
Youku API Python SDK / 优酷 API Python 客户端

优酷 API Python 客户端比较完整地实现了优酷开放平台官方的各种 API，具体功能和对应的类分别是：
* 视频上传 (Video Upload) ，支持中断续传，YoukuUpload
* OAuth2 授权，YoukuOauth
* 用户(users)，YoukuUsers
* 评论(comments)，YoukuComments
* 视频(videos)，YoukuVideos
* 节目(shows)，YoukuShows
* 专辑(playlists)，YoukuPlaylists
* 搜索(searches)，YoukuSearchs
* 人物(persons)，YoukuPersons
* 数据约束(schemas)，YoukuSchemas

注：本客户端**不支持**优酷视频下载功能，一方面官方 API 就不支持，另一方面已经
有很多第三方库实现了视频下载功能。

已在 Python 2.6.x 以上测试过，未测试过 Python 3.

各种 API 细节，如参数、返回值等请参考[优酷 API 官方文档](http://open.youku.com/docs/doc?id=0)和源码，基本上都是一一对应的。

本客户端依赖的第三方库只有 requests，请事先安装，例如<code>pip install requests</code>

基本说明：
各个功能分别对应本包中的相应模块。


上传功能使用示例：
```
from youku import YoukuUpload

def main():
    file_info = {
      'title': u'Google I/O 2014'
      'tags': 'Google,IO',
      'description': 'I/O Keynote'
    }
    file = '/home/hanguokai/filename.mp4'
    youku = YoukuUpload(CLIENT_ID, ACCESS_TOKEN, file)
    youku.upload(file_info)
```

因为上传包含内部状态，所以每个上传文件需要新建一个 YoukuUpload 对象，并在一个线程中执行。
其它各功能 API 都是简单的无状态 REST 调用，所有请求只需要构建一个对象使用即可。

异常处理，所有功能产生的异常都会抛出 YoukuError 异常对象，表示优酷官方定义的异常。异常对象包括如下属性
* status_code，返回的 HTTP 状态码
* code，错误码
* type，错误类型
* description，错误描述
