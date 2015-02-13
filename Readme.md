#NYT Chinese Recipe

这是一个基于 [KindleEar](https://github.com/cdhigh/kindleear) 项目的 Recipe，支持将[纽约时报中文网](http://cn.nytimes.com/) RSS 内过去七天内的文章打包发送到 Kindle 设备。

##依存关系

- Google App Engine
- KindleEar
- Python 2.7.8

##安装方法

- 将 NYTChinese.py 脚本文件放在 books 文件夹
- 将 `cv_nytchinese.jpg` 和 `mh_nytchinese.gif` 两个图片文件放在 images 文件夹
- 重新部署 Kindle Ear
- 刷新 Kindle Ear 首页，此图书会自动安装。

##卸载方法

- 从 books 文件夹中删除 NYTChinese.py 脚本文件
- 从 images 文件夹中删除 `cv_nytchinese.jpg` 和 `mh_nytchinese.gif` 两个图片文件
- 重新部署 Kindle Ear
- 图书会在一天之后自动从 Kindle Ear 系统内删除

###如果需要立即生效，可以继续这么做：

- 登录到 App Engine 控制面板，在 Data 选项下点击“Datastore Viewer”
- 在 Query 选项卡的下拉菜单里选择 Book，删掉 title 为“纽约时报中文网”的 Book 记录即可

##版权声明

`cv_nytchinese.jpg` 和 `mh_nytchinese.gif` 两个图片文件使用了[纽约时报公司](http://www.nytimes.com/)的商标，版权属于纽约时报公司所有。

##授权

Licensed under the Apache License, Version 2.0

##其他

有疑问，请与我联系： [@bfishadow](https://twitter.com/bfishadow)
