# MyToys

记录了一些使用 Selenium 和 Scrapy 进行数据爬取的学习demo

感谢在一路上给我帮助的朋友们~

--------------
2021年2月24日

&emsp;年初的时候就有了做这个项目的想法，但是当时自己对爬虫压根一窍不通，于是便开始了自己的受苦之旅哈哈哈哈

&emsp;最开始想用 request 进行数据爬取，结果发现人家是JS渲染，压根获得不到页面源代码。
计划一：卒

&emsp;后来使用 Selenium 模拟浏览器进行数据爬取，但是很快就发现自己的 IP 被封了，当时还不知道有 IP池 这个东西哈哈哈，然后学了一下怎么加IP池和报头。很快又遇到一个问题：速度实在是太慢了！
计划二：卒

&emsp;兜兜转转又回到了计划一，由于我对JS渲染压根没接触过，所以有些恐惧，但是为了自己的钱包和锻炼自己面对困难、解决困难的能力，下定决心硬着头皮上，跳出舒适区！

&emsp;我记得那天晚上查了很久也没有解决这个问题，正准备休息睡觉，突然间看到一篇很有用处的博客，于是我学会了怎么抓包并且以此来获得页面的JSON文件，于是计划一：通！


&emsp;果然遇到问题的时候，解决问题才是唯一的选择！

---------------
需求列表：

1：优化代码，使代码可读性更好

2：增加【根据时间生成文件名称】功能

3：增加【数据库】
