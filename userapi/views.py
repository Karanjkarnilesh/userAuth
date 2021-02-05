
from django.shortcuts import render

from rest_framework.decorators import APIView
from rest_framework.response import Response
import re
from .models import UserModel
# Create your views here.

def get_single_user(email,password):
    user_object = UserModel.objects.filter(Email=email, Password=password)
    return user_object



def update_user(user_object, data):
    if "username" in data:
        user_object.UserName = data['username']
    
    if "email" in data:
        user_object.Email = data['email']

    if "mobile" in data:
        user_object.Mobile = data['mobile']

    if "password" in data:
        user_object.Password = data['password']

    print("end if")
    
    user_object.save()
    return user_object


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
            # email = request.data['email']
            # password = request.data['password']
            email="karanjkar.nk@gmail.com"
            password="4545"
            #  check with databse check filter or get
            user=get_single_user(email,password)
            if user:
                return Response("Login successfuly")

            return Response("Plz First Signup user is not present")

    def delete(self, request, username=None):
        if request.method == "DELETE":
            userdata = request.data['userdata']
            user = delete_user(userdata)
            user.delete()
            return Response("Delete Successfully")

    def put(self, request, username="karanjkar"):
        user_object = UserModel.objects.get(UserName=username)
        if user_object:
            userChange = request.data['password']
            update = update_user(user_object, userChange)
            return Response("ALL Clear")
