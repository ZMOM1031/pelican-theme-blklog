#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'ZMOM1031'
SITENAME = u'IterNull - Blog'
SITEURL = 'https://blog.iternull.com'

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'
DEFAULT_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

DEFAULT_LANG = u'cn'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Articles
ARTICLE_PATHS = ['posts']
ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'

# Pages
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

# Tags
TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'
#TAGS_URL = 'tags/'
#TAGS_SAVE_AS = 'tags/index.html'

# Authors
AUTHOR_URL = 'author/{slug}/'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'
#AUTHORS_URL = 'authors/'
#AUTHORS_SAVE_AS = 'authors/index.html'

# Category
CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
#CATEGORYS_URL = 'categories/'
#CATEGORYS_SAVE_AS = 'categories/index.html'

# Index Pages
#DEFAULT_ORPHANS (0)
DEFAULT_PAGINATION = 20
PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)

# Others
DISQUS_SITENAME = ''
DUOSHUO_SITENAME = ''
GITHUB_URL = 'https://github.com/ZMOM1031'

# Meun
MEUN = (('Home', '/'),
		('About', '/about'),
		('Archives', '/archives.html'),
)

# Blogroll
LINKS = (#("IterNull", "http://www.iternull.com/"),
         #("TYPCN Tech", "http://blog.eqoe.cn/"),
         ("音符の新世界", "http://freedom.moe/"),
         #("YsiCing", 'http://ysicing.net/'),
         #("吾爱笔记", 'http://www.ist-802.net/'),
         ("YsiCing's Blog", "https://ysicing.net/"),
         ("Vtrois's Blog", "http://www.vtrois.com/"),
         ("往前方", "http://www.wangqianfang.com/"),
         #("涛涛的痕迹", "https://www.liujiantao.me/"),
         ("Yay Ka-Boom-Boom", "https://www.lynx.im/"),
)

# Social widget
SOCIAL = (('Weibo', 'http://weibo.com/2655123364'),
          ('Twitter', 'https://twitter.com/ZMOM1031'),
          ('GitHub', 'https://github.com/ZMOM1031'),
)

# Projects
PROJECTS = (("NetHunter 安装工具", "https://github.com/ZMOM1031/NetHunter-Install-Tools"),
			("LAN Tap", "https://github.com/ZMOM1031/lan-tap"),
)

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Theming
THEME = 'themes/blklog'

# Plugins
#PLUGIN_PATHS = ['plugins']
#PLUGINS = [
#			'sitemap',
#			'yuicompressor'
#]

# Static paths will be copied under the same name
STATIC_PATHS = [
				'data',
				'pub', 
                'p',
                'favicon.ico', 
                '404.html', 
                'robots.txt', 
                'CNAME', 
                'README.md'
]

EXTRA_PATH_METADATA = {
						'robots.txt': {'path': 'robots.txt'},
                        'favicon.ico': {'path': 'favicon.ico'}
}

# Sitemap settings
#SITEMAP = {
#    'format': 'xml',
#    'priorities': {
#        'articles': 0.5,
#        'indexes': 0.5,
#        'pages': 0.5
#    },
#    'changefreqs': {
#        'articles': 'monthly',
#        'indexes': 'daily',
#        'pages': 'monthly'
#    }
#}
