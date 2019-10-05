#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2019/9/16 0:38
@Author:  LQ
@Email: LQ65534@163.com
@File: adminx.py
@Software: PyCharm

# 富文本编辑器集成 https://www.cnblogs.com/zhangguanghe/articles/9230512.html
"""
import xadmin
from .models import FirstCatage, SecondCatage


class FirstCatageAdmin(object):
    list_display = ("first_catage_slug", "first_catage_order", 'first_catage_title', "add_time")  # 在后台列表下显示的字段


xadmin.site.register(FirstCatage, FirstCatageAdmin)


class SecondCatageAdmin(object):
    list_display = (
        "second_catage_slug", "second_catage_order", 'second_catage_title', 'second_catage_type',
        "add_time")  # 在后台列表下显示的字段
    style_fields = {"second_catage_html": "ueditor"}
    search_fields = ["second_catage_slug", "second_catage_order", "second_catage_title"]
    # 配置筛选字段
    list_filter = ["second_catage_slug", 'second_catage_title', "second_catage_order", 'second_catage_type', "add_time"]


xadmin.site.register(SecondCatage, SecondCatageAdmin)

# xadmin全局配置
from xadmin import views


# 创建X admin的全局管理器并与view绑定。
class BaseSetting(object):
    # 开启主题功能
    enable_themes = True
    use_bootswatch = True


# xadmin全局配置
class GlobalSettings(object):
    site_title = "后台管理"
    site_footer = "管理系统"

    # 让管理后台左侧收起来
    # menu_style = "accordion"


# 将全局配置管理与view绑定注册
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)

if __name__ == "__main__":
    pass
