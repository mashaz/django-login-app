#coding=utf-8
from django.shortcuts import render,render_to_response
from django.http import HttpResponseRedirect
from users.models import User
from django import forms
from django.http import HttpResponse


#定义表单模型
class UserForm(forms.Form):
    username = forms.CharField(label='用户名：',max_length=100)
    password = forms.CharField(label='密码：',widget=forms.PasswordInput())

#登录
def login(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            #获取表单用户密码
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            #获取的表单数据与数据库进行比较
            user = User.objects.filter(username__exact = username,password__exact = password)
            if user:
                request.session['username'] = username
                return HttpResponseRedirect('/')
            else:
                user_by_email = User.objects.filter(email__exact = username,password__exact = password)
                if user_by_email:
                    request.session['username'] = user_by_email[0].username
                    return HttpResponseRedirect('/')
                else:
                    context = {}
                    context['invid'] = 'invid'
                    return render(request, 'login.html', context)

    return render_to_response('login.html')

def logout(request):
    try:
        del request.session['username']
    except KeyError:
        pass
    return HttpResponseRedirect('/')

def is_username_legal(username):
    if len(username) < 4 :
        return 0
    elif ' ' in username:
        return 0
    elif '.' in username:
        return 0
    elif ',' in username:
        return 0
    elif '-' in username:
        return 0
    else:
        return 1
def is_password_legal(password):
    if len(password) < 6 :
        return 0
    else:
        return 1
def register(request):
    if request.method == 'POST':
        context = {}
        username = request.POST['username'].encode('utf-8')
        if is_username_legal(username) == 0:
            context['illegal_username'] = 1
            return render(request,'register.html',context)
        password = request.POST['password'].encode('utf-8')
        if is_password_legal(password) == 0:
            context['illegal_password'] = 1
            return render(request,'register.html',context)
        email = request.POST['email'].encode('utf-8')
        user = User.objects.filter(username=username)

        
        if len(user)==0:
            user = User()
            user.username = username
            user.password = password
            user.email = email
            user.save()
            # todo 判断username email
            
            context['register_flag'] = 'register succeed'
            context['register_username'] = username
            return render(request,'login.html',context)

        elif  user[0].username == username:
            context['exist_username'] = 1
            return render(request,'register.html',context)

        else:
            user = User.objects.filter(email=email)
            if user[0].email == email:
                context['exist_email'] = 1
                return render(request,'register.html',context)
           

                

    else:
        return render_to_response('register.html')
def info(request):
    return render(request,'userinfo.html')