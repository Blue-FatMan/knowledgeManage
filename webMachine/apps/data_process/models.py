from django.db import models
from datetime import datetime
from DjangoUeditor.models import UEditorField


# Create your models here.
# https://www.cnblogs.com/baishuchao/p/9291344.html
# https://www.cnblogs.com/zhangguanghe/articles/9230512.html


class FirstCatage(models.Model):
    First_Catage_Name = (("1", '监督学习'), ("2", '无监督学习'), ("3", '模型选择和评估'), ("4", '检验'), ("5", '数据集转换'),
                         ("6", '数据加载工具'), ("7", '使用sklearn计算'))
    first_catage_slug = models.SlugField(verbose_name="一级目录连接", max_length=50, null=False, blank=False, unique=True,
                                         help_text='一级目录连接,禁止为空,禁止重复')
    first_catage_title = models.CharField(verbose_name="一级目录名称", max_length=50, null=False, blank=False,
                                          help_text='一级目录名称,禁止为空')
    first_catage_order = models.DecimalField(verbose_name="一级目录顺序", max_digits=5, decimal_places=2, null=True,
                                             blank=True,
                                             help_text="一级目录顺序，决定前端目录顺序,允许为空")
    add_time = models.DateTimeField(verbose_name="添加时间", default=datetime.now)

    class Meta:
        verbose_name = '一级目录'
        verbose_name_plural = verbose_name
        ordering = ["first_catage_order"]

    def __str__(self):
        return self.first_catage_title
    #
    # def __unicode__(self):
    #     return self.first_catage_title


class SecondCatage(models.Model):
    second_catage_title = models.CharField(verbose_name="二级目录名称", max_length=50, null=False, blank=False,
                                           help_text='二级目录名称,禁止为空')
    second_catage_order = models.DecimalField(verbose_name="二级目录顺序", max_digits=5, decimal_places=2, null=True,
                                              blank=True,
                                              help_text="二级目录顺序，决定前端目录顺序,允许为空")
    second_catage_type = models.ForeignKey(FirstCatage, verbose_name="二级目录类型", related_name="second_catage_type",
                                           default="未设置二级目录类型", blank=False, null=False, on_delete=models.SET_DEFAULT)
    second_catage_slug = models.SlugField(verbose_name="二级目录连接", max_length=50, null=False, blank=False, unique=True,
                                          help_text='二级目录连接,禁止为空,禁止重复')
    second_catage_html = UEditorField(verbose_name="二级目录详细介绍", null=False, blank=False,
                                      help_text='二级目录主页,禁止为空',
                                      toolbars="full",
                                      imagePath="second_catage/ueditor/", filePath="second_catage/ueditor/", )
    add_time = models.DateTimeField(verbose_name="添加时间", default=datetime.now)

    def get_second_catage_html(self):
        return self.second_catage_html

    class Meta:
        verbose_name = '二级目录'
        verbose_name_plural = verbose_name
        ordering = ["second_catage_order"]

    def __str__(self):
        return self.second_catage_title
