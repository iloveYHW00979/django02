from django.http import HttpResponse, request
import requests
from django.http.response import JsonResponse
from django.shortcuts import render
from .models import *
from rest_framework.views import APIView
from .serializers import *
import re
import json
#用户登录
class User_login_view(APIView):
    def get(self, request):
        user_name = request.GET.get('user_name')
        print(user_name)
        return HttpResponse({"66": "88"})
    def post(self, request):
        user_name = request.data.get('user_name')
        password = request.data.get('password')
        try:
            user = User.objects.filter(user_name=user_name, password=password)
            print(user_name, password)
            if user:
                date_msg = "登陆成功"
                date_flag = 'yes'
                date = {'flag': date_flag, 'msg': date_msg}
                return HttpResponse(json.dumps({"request": date}, ensure_ascii=False))
            else:
                return HttpResponse({'登陆失败':''})

        except Exception as e:
            return HttpResponse({"77": "99"})


class Session_test_view(APIView):
    def session_test(self, request):
        request.session['h1'] = 'hello'#设置键和值
        return HttpResponse('写session')


class News_list_view(APIView):#主页新闻标题列表
    def get(self, request):
        news = News.objects.filter().all()
        # print(type(news))
        serializer = NewsSerializers(news, many=True)
        # print(serializer.data)
        return HttpResponse(json.dumps({'data': serializer.data}, ensure_ascii=False), 'application/json')

class Team_ranking_view(APIView):#团队排名
    def get(self, request):
        team_rank = TeamRanking.objects.filter().order_by('rank_id')
        serializer = Team_RankingSerializers(team_rank, many=True)
        data = serializer.data
        return HttpResponse(json.dumps({'data': serializer.data}, ensure_ascii=False), 'application/json')

class Index_Equipment_view(APIView):#设备展示
    def get(self, request):
        imgs = AllImg.objects.filter(img_id=1)
        serializer = All_imgsSerializers(imgs, many=True)
        return HttpResponse(json.dumps({'data': serializer.data}, ensure_ascii=False), 'application/json')

class Culture_routimg_view(APIView):#公司文化轮播图
    def get(self, request):
        imgs = AllImg.objects.filter(img_id=2)
        serializer = All_imgsSerializers(imgs, many=True)
        # print(serializer.data)
        return HttpResponse(json.dumps({'data': serializer.data}, ensure_ascii=False), 'application/json')

class Inc_introduce_view(APIView):#公司介绍
    def get(self, request):
        inc_introduce = IncIntroduce.objects.filter()
        serializer = Inc_introduceSerializers(inc_introduce, many=True)
        # print(serializer.data)
        return HttpResponse(json.dumps({'data': serializer.data}, ensure_ascii=False), 'application/json')

class Culture_view(APIView):
    def get(self, request):
        culture_ = Culture.objects.filter()
        serializer = CultureSerializers(culture_, many=True)
        return HttpResponse(json.dumps({'data': serializer.data}, ensure_ascii=False), 'application/json')

class All_Equipment_view(APIView):
    def get(self, request):
        equipment_ = Equipment.objects.filter().order_by('update')
        serializer = EquipmentSerializers(equipment_, many=True)
        return HttpResponse(json.dumps({'data': serializer.data}, ensure_ascii=False), 'application/json')

class Index_routa_view(APIView):
    def get(self, request):
        Index_routa_img = AllImg.objects.filter(img_id='5')
        serializer = All_imgsSerializers(Index_Equipment_view)
