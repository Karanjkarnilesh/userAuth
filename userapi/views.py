from django.shortcuts import render
from rest_framework.decorators import APIView
from rest_framework.response import Response
import re
from .models import UserModel
# Create your views here.


def isValid(s):
    # 1) Begins with 0 or 91
    # 2) Then contains 7 or 8 or 9.
    # 3) Then contains 9 digits
    Pattern = re.compile("(0/91)?[7-9][0-9]{9}")
    return Pattern.match(s)


def delete_user(username):
    try:
        user_object = UserModel.objects.filter(UserName=username).first()
        return user_object
    except Exception as e:
        return None


class User(APIView):
    def post(self, request):
        # if request.method=="post":
        username = request.data['username']
        email = request.data['email']
        mobile = request.data['mobile']
        password = request.data['password']
        confpassword = request.data['confpassword']
        if password != confpassword:
            return Response("password is not correct")
        elif(not isValid(mobile)):
            return Response("Invalid number")
        # user_object=UserModel.objects.create(userName=username,Email=email,Mobile=mobile,Password=password)
        # user_object.save()
        return Response("Signup Scessfully")

    def get(self, request):
        if request.method == "GET":
            email = request.data['email']
            password = request.data['password']
            #  check with databse check filter or get
            user_object = UserModel.objects.filter(Email=email, Password=password)
            if user_object:
                return Response("Login successfuly")
            
            return Response("Plz First Signup user is not present")
            

    def delete(self, request, userid=None):
        if request.method == "DELETE":
            userdata = request.data['userdata']
            user = delete_user(userdata)
            user.delete()
            return Response("Delete Successfully")

    def put(self, request, userid=None):
        if request.method == "PUT":
            pass
