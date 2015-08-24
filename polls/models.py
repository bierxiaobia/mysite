# -*-coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
import logging
from ckeditor.fields import RichTextField

# Create your models here.


class User(AbstractUser):
    ROLE_CHOICES = (
        (0, "管理员"),
        (1, "普通用户"),
        (2, "总编"),
    )

    NORMAL = 1
    EDITOR = 2
    SUPERUSER = 0

    role = models.IntegerField(verbose_name=u'用户角色', choices=ROLE_CHOICES, default=1)

    class Meta:
        app_label = 'polls'

    @classmethod
    def user_login(cls, username, passwd):
        if username and passwd:
            return "error: 用户名或密码为空"
        kwargs = {
            'username': username,
            'password': passwd
        }
        result = cls.objects.filter(**kwargs)
        if result:
            return "success"

        return "用户名不存在或密码有误"


class Picture(models.Model):

    name = models.CharField(verbose_name=u'名称', max_length=128, )
    dire = models.CharField(verbose_name=u'图片地址', max_length=200)
    desc = models.TextField(verbose_name=u'简介', max_length=200, null=True)
    addr = models.CharField(verbose_name=u'地点', max_length=200, null=True)
    article = models.ForeignKey('Article', null=True)
    created_time = models.DateTimeField(verbose_name=u'时间', auto_now_add=True, db_index=True)

    class Meta:
        app_label = 'polls'

    @classmethod
    def add(cls, name='', dire='', desc='', addr='', article=None):
        if not name:
            return False
        try:
            ob = cls()
            ob.name = name
            ob.dire = dire
            ob.desc = desc
            ob.addr = addr
            ob.article = article
            ob.save()
            return True
        except Exception, e:
            logging.error(e)
            return False

    @classmethod
    def query(cls):
        try:
            results = cls.objects.all()
            return results
        except Exception, e:
            logging.error(e, desc='cannot get picture results')
            return []


class Article(models.Model):

    title = models.CharField(verbose_name=u'题目', max_length=200)
    content = RichTextField(u'正文', config_name='default')
    addr = models.CharField(verbose_name=u'地点', max_length=200, null=True)
    created_at = models.DateTimeField(verbose_name=u'时间', auto_now_add=True, db_index=True)

    created_at = datetime.now()

    class Meta:
        app_label = 'polls'

    @classmethod
    def query(cls, aid=0):
        try:
            if aid:
                result = cls.objects.get(id=aid)
            else:
                raise Exception
        except Exception, e:
            return None

    @classmethod
    def query_all(cls):
        try:
            result = cls.objects.all()
            return result
        except Exception, e:
            logging.error(e)
            return []

    @classmethod
    def add(cls, title, content=''):
        try:
            article = cls()
            article.title = title
            article.content = content
            article.created_at = datetime.now()
            article.save()
            return True
        except Exception, e:
            logging.error(e)
            return False







