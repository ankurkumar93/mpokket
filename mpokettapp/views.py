from curses.ascii import US
from django.http import HttpResponse
from django.shortcuts import render
from httplib2 import Http
from rest_framework.views import APIView
from .models import User
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
import csv
import mysql.connector

class Home(APIView):
    def get(self,request):
        message = {'Message':'Type getuserview in URL followed by id to get data'}
        return Response(message, status=HTTP_200_OK)


class GetUserView(APIView):

    def get(self, request, id, fmt=None):
        context = {}
        conn = mysql.connector.connect(user = 'candidate',
                               host = '165.22.222.199',
                              database = 'extdb', password='NSDwL8gfr8Xg')
        cursor = conn.cursor()

        try:
            sql = 'select * from tbl_users where id={}'.format(id)
            cursor.execute(sql)
            user = cursor.fetchone()
            context['id'] = user[0]
            context['name'] = user[9]
            context['mobile'] = user[3]
            context['email'] = user[2]
            if fmt is None:
                return Response(context, status=HTTP_200_OK)
            conn.close()
        except:
            message = {
                'User': 'User with that id is not found'
            }
            return Response(message, status=HTTP_200_OK)
        return render(request, 'csv.html', context=context) 
