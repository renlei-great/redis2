from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def set_sessions(request):
    request.session['username'] = 'renlei'
    request.session['password'] = '1234'

    return HttpResponse('设置成功')


def get_sessions(request):
    name = request.session['username']
    pwd = request.session['password']

    return HttpResponse('用户名是：'+ name + '密码是' + pwd)


def jj():
    pass
