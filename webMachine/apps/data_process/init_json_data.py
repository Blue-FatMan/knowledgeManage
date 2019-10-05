#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2019/10/4 9:37
@Author:  LQ
@Email: LQ65534@163.com
@File: init_json_data.py
@Software: PyCharm

# 该py文件返回index页面初始化请求的json，也就是返回整个网站前端初始化所需数据
"""
from django.views.generic.base import View
from django.http import HttpResponse, JsonResponse
import json
from .models import FirstCatage, SecondCatage
import os

base_dir = os.path.dirname(os.path.abspath(__file__))


class InitJsonData(View):
    def get(self, request):
        with open(os.path.join(base_dir,"init.json"), "r",
                  encoding="utf-8") as fr:
            init_json = json.load(fr)
        # json 格式如下
        # doc_first_child_dict = {
        # 					"title": "主页一",
        # 					"href": "page/welcome-1.html",
        # 					"icon": "fa fa-tachometer",
        # 					"target": "_self"
        # 				}
        # doc_first_dict = {"title": "数据集转换",
        # 			      "href": "",
        # 			      "icon": "fa fa-home",
        # 			      "target": "_self",
        #                 "child": [doc_first_child_dict]}
        # document_child = {"child": [doc_first_dict]}
        first_menu_list = FirstCatage.objects.all()
        if first_menu_list:
            document_child_dict = {"child": []}
            for first_obj in first_menu_list:
                doc_first_dict = {}
                first_catage_title = first_obj.first_catage_title
                first_catage_slug = first_obj.first_catage_slug
                doc_first_dict["title"] = first_catage_title
                doc_first_dict["href"] = ""
                doc_first_dict["icon"] = "fa fa-home"
                doc_first_dict["target"] = "_self"
                doc_first_dict["child"] = []
                second_catage_obj = first_obj.second_catage_type.all()
                if second_catage_obj:
                    for second_catage in second_catage_obj:
                        doc_first_child_dict = {}
                        second_catage_title = second_catage.second_catage_title
                        second_catage_href = second_catage.second_catage_slug
                        doc_first_child_dict["title"] = second_catage_title
                        doc_first_child_dict["href"] = r"datapage/" + first_catage_slug + "/" + second_catage_href
                        doc_first_child_dict["icon"] = "fa fa-tachometer",
                        doc_first_child_dict["target"] = "_self"
                        doc_first_dict["child"].append(doc_first_child_dict)
                document_child_dict["child"].append(doc_first_dict)
            init_json["menuInfo"]["document"].update(document_child_dict)
        # obj[4].second_catage_type.all()[0].second_catage_title
        return HttpResponse(JsonResponse(init_json), content_type="application/json")
