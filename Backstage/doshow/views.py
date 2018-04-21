from django.shortcuts import render
import time,datetime
from django.shortcuts import HttpResponse
from django.shortcuts import redirect
import json
from doshow import models
from doshow.doshow_lib import Verification_Form

def bxslider(request):
    obj = models.Bxslider.objects.filter(status=0).values('img_url','href','name')
    return render(request,'bxslider.html',{'obj':obj})
def index(request):
    if request.method == "POST":
        tbl = request.POST.get('tbl')
        if tbl == "dw_money_flow":
            consume_type = request.POST.get('consume_type')
            order_id = request.POST.get('order_id')
            consume_uin = request.POST.get('consume_uin')
            accept_uin = request.POST.get('accept_uin')
            payment_id = request.POST.get('payment_id')
            fee = request.POST.get('fee')
            money = request.POST.get('money')
            before_money = request.POST.get('before_money')
            after_money = request.POST.get('after_money')
            make = '用户充值ֵ'
            create_time = time.time()
            state = 1
            state_time = time.time()
            appflag = 1
            return HttpResponse('充值成功！')

    elif request.method == "GET":
        return render(request,'index.html')


def home(request):
    if request.method == "POST":
        return HttpResponse('method error')
    elif request.method == 'GET':
        if request.session.get('login',None):
            return render(request,'home.html',{'user':request.session['username']})
        else:
            return redirect('/login/')
    else:
        return HttpResponse('method error')

def login(request):
    error_msg = ''
    if request.method == "POST":
        username = request.POST.get('username',None).strip()
        password = request.POST.get('password',None).strip()
        V1 = Verification_Form.Form_verification(username)
        V2 = Verification_Form.Form_verification(password)
        if V1.username_V(4,20):
            if V2.password_V(6,20,0):
                exist = models.UserInfo.objects.filter(username=username,password=password).first()
                if exist:
                    request.session['username'] = username
                    request.session['login'] = True
                    request.session.set_expiry(0)
                    return redirect('/home/')
                else:
                    error_msg = "用户名或密码输入错误！"
                    return render(request,'login.html',{'error_msg':error_msg})
            else:
                error_msg = '用户名或密码格式错误！'
                return render(request,'login.html',{'error_msg':error_msg})
        else:
            error_msg = '用户名或密码格式错误！'
            return render(request,'login.html',{'error_msg':error_msg})
    elif request.method == "GET":
        return render(request,'login.html',{'error_msg':error_msg})
    else:
        return HttpResponse('method error')

def register(request):
    error_msg = ""
    if request.method == "POST":
        username = request.POST.get('username',None).strip()
        password = request.POST.get('password',None).strip()
        V1 = Verification_Form.Form_verification(username)
        V2 = Verification_Form.Form_verification(password)
        if V1.username_V(4,20):
            if V2.password_V(6,20,0):
                exist = models.UserInfo.objects.filter(username=username).first()
                if exist:
                    error_msg = '用户名已存在！'
                    return render(request,'register.html',{'error_msg':error_msg})
                else:
                    dict_1 = {}
                    dict_1['username'] = username
                    dict_1['password'] = password
                    models.UserInfo.objects.create(**dict_1)
                    return redirect('/login/')
            else:
                error_msg = '用户名或密码格式错误！'
                return render(request,'register.html',{'error_msg':error_msg})
        else:
            error_msg = '用户名或密码格式错误！'
            return render(request,'register.html',{'error_msg':error_msg})
    elif request.method == "GET":
        return render(request,'register.html',{'error_msg':error_msg})
    else:
        return HttpResponse('method error')

def logout(request):
    request.session.clear()
    return redirect('/login/')

def modify(request):
    if request.method == "POST":
        username = request.POST.get('username',None).strip()
        password_1 = request.POST.get('password_1',None).strip()
        password_2 = request.POST.get('password_2',None).strip()
        password_3 = request.POST.get('password_3',None).strip()
        V1 = Verification_Form.Form_verification(username)
        V2 = Verification_Form.Form_verification(password_1)
        if V1.username_V(4,20):
            if V2.password_V(6,20,0):
                exist = models.UserInfo.objects.filter(username=username,password=password_1).first()
                if exist:
                    if password_2 == password_3:
                        V3 = Verification_Form.Form_verification(password_3)
                        if V3.password_V(6,20,0):
                            models.UserInfo.objects.filter(username=username).update(password=password_3)
                            return HttpResponse('OK')
                        else:
                            return HttpResponse('新密码格式错误！')
                    else:
                        return HttpResponse('两次密码输入不一致！')
                else:
                    return HttpResponse('用户名密码验证失败！')
            else:
                return HttpResponse('用户名密码验证失败！')
        else:
            return HttpResponse('用户名密码验证失败！')
    elif request.method == "GET":
        return render(request,'modify.html')
    else:
        return HttpResponse('method error!')

def three_one(request):
    if request.method == "POST":
        uin_3_1 = request.POST.get('uin_3_1',None).strip()
        password_new = request.POST.get('password_new',None).strip()
        password_new_con = request.POST.get('password_new_con',None).strip()
        reason = request.POST.get('reason',None).strip()

        if uin_3_1 == "" or password_new == "" or password_new_con == "" or reason == "":
            return HttpResponse('error_none')
        return HttpResponse('OK')

    elif request.method == "GET":
        return HttpResponse('500')
    else:
        return HttpResponse('500')

data = []
for i in range(1,671):
    a = {}
    a['id'] = str(i)
    a['key_1'] = 'value_' + str(i)
    a['key_2'] = 'value_' + str(i)
    a['key_3'] = 'value_' + str(i)
    a['key_4'] = 'value_' + str(i)
    a['key_5'] = 'value_' + str(i)
    a['key_6'] = 'value_' + str(i)
    a['key_7'] = 'value_' + str(i)
    a['key_8'] = 'value_' + str(i)
    data.insert(i-1,a)

def one_one(request):
    if request.method == "POST":
        from_page = request.POST.get('from_page')
        if from_page == '1.1':
            start_time = request.POST.get('start_time',None).strip()
            end_time = request.POST.get('end_time',None).strip()
            if start_time == '' or end_time == '':
                return HttpResponse('date_error')
            else:
                start_time_list = start_time.split()
                # 将"2018-04-17 00:00:00" 切割成 ['2018-04-17,'00:00:00']
                start_time_date = datetime.datetime.strptime(start_time_list[0],'%Y-%m-%d')
                # 将"2018-04-17" 转换成 "datetime.datetime(2018, 4, 17, 0, 0)" datetime类型，用于时间之间运算
                end_time_list = end_time.split()
                end_time_date = datetime.datetime.strptime(end_time_list[0],'%Y-%m-%d')

                time_diff = end_time_date - start_time_date         #算出时间差
                time_diff = time_diff.days                          #格式是int，有负数
                if time_diff < 0 or time_diff > 30:
                    return HttpResponse('date_range_error')
                else:
                    uin = request.POST.get('uin',None).strip()
                    order_type = request.POST.get('order_type',None).strip()
                    sale_type = request.POST.get('sale_type',None).strip()
                    status = request.POST.get('status',None).strip()
                    payment_type = request.POST.get('payment_type',None).strip()
                    full_network_parment_uin = request.POST.get('full_network_parment_uin',None).strip()
                    proxy_room_id = request.POST.get('proxy_room_id',None).strip()
                    proxy_uin = request.POST.get('proxy_uin',None).strip()
                    order_id = request.POST.get('order_id',None).strip()
                    dict_1_1 = {}
                    dict_1_1['start_time'] = start_time
                    dict_1_1['end_time'] = end_time
                    dict_1_1['uin'] = uin
                    dict_1_1['order_type'] = order_type
                    dict_1_1['sale_type'] = sale_type
                    dict_1_1['status'] = status
                    dict_1_1['payment_type'] = payment_type
                    dict_1_1['full_network_parment_uin'] = full_network_parment_uin
                    dict_1_1['proxy_room_id'] = proxy_room_id
                    dict_1_1['proxy_uin'] = proxy_uin
                    dict_1_1['order_id'] = order_id
                    data_1 = json.dumps(data)
                    return HttpResponse(data_1)
    elif request.method == "GET":
        return HttpResponse('500')
    else:
        return HttpResponse('500')


