# -*- coding: utf-8 -*-
"""SiHuan博客构建配置文件
"""

# For Maverick
site_prefix = "/"
template = {
    "name": "Galileo",
    "type": "git",
    "url": "https://github.com/Si-Huan/Maverick-Theme-Galileo.git",
    "branch": "latest"
}
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20
enable_jsdelivr = {
    "enabled": True,
    "repo": "Si-Huan/SiHuan-Blog@gh-pages"
}

# 站点设置
site_name = "SiHuan's Blog"
site_logo = "${static_prefix}logo.png"
site_build_date = "2020-01-01T00:00+08:00"
author = "SiHuan"
email = "sihuan@sakuya.love"
author_homepage = "https://www.sakuya.love"
description = "道阻且长，君子思还。"
key_words = ['SiHuan', '思还', 'Blog', '博客', 'GitBlog']
language = 'zh-CN'
external_links = [
    {
        "name": "SiHuan-Wiki",
        "url": "http://wiki.sakuya.love",
        "brief": "我的知识积累。"
    }
]
nav = [
    {
        "name": "首页",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "归档",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "縁起",
        "url": "${site_prefix}enngi/",
        "target": "_self"
    }
]

social_links = [
    {
        "name": "Telegram",
        "url": "https://t.me/Si_Huan",
        "icon": "gi gi-telegram"
    },
    {
        "name": "GitHub",
        "url": "https://github.com/Si-Huan",
        "icon": "gi gi-github"
    }
    # ,
    # {
    #     "name": "QQ",
    #     "url": "https://weibo.com/5245109677/",
    #     "icon": "gi gi-twitter"
    # }
]

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
'''

footer_addon = ''

body_addon = ''
