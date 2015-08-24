# coding=utf-8
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from PIL import Image
from models import User, Picture, Article
import ImageFile

UPLOAD_PATH = '/Users/wangxue/PycharmProjects/mysite/mysite/statics/upload'


def login(request):
    query_dict = request.GET
    user_name = query_dict.get('username', '')
    passwd = query_dict.get('passwd', '')
    # 验证用户登录信息
    info = User.user_login(user_name, passwd)
    result = False
    if info == "success":
        result = True
    return render(request, "home.html", {'result': result, 'info': info})


def home(request):
    query_dict = request.GET
    data = dict()
    pictrues = Picture.query()
    data.update({'pictures': pictrues})
    return render(request, 'home.html', data)


def picture(request):
    data = dict()
    pictrues = Picture.query()
    data.update({'pictures': pictrues})
    return render(request, 'picture.html', data)


def picture_add(request):
    qd = request.GET
    data = dict()
    return render(request, 'picture_add.html', data)


def save_picture(request):
    try:

        qd = request.POST
        name = qd.get('name', '')
        desc = qd.get('desc', '')
        reqfile = request.FILES['picfile']  # picfile要和html里面一致
        img = Image.open(reqfile)
        img.thumbnail((500, 500), Image.ANTIALIAS)  # 对图片进行等比缩放
        img.save("{0}/{1}.png".format(UPLOAD_PATH, name), "png")  # 保存图片
        dire = "{0}.png".format(name)
        Picture.add(name=name, dire=dire, desc=desc)

        return render(request, 'picture.html', {})

    except Exception, e:
        return HttpResponse("Error %s" % e)  # 异常，查看报错信息


def article(request):
    qd = request.GET
    data = dict()
    return render(request, 'article.html', data)


def article_list(request):
    result = Article.query_all()
    data = {'result': result}
    return render(request, 'article_list.html', data)


def article_add(request):
    qd = request.POST
    content = qd.get('editor', '')
    title = qd.get('title', '')
    Article.add(title, content)
    return HttpResponseRedirect('list_article')


def technich(request):
    qd = request.GET
    data = dict()
    return render(request, 'technich.html', data)

def wirtedown(request):

    return render(request, 'article.html', {})
