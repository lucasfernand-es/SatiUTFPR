from django import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db import models


class LoginController:

    def __init__(self, request):
        self.username = "username";


    def newLogin(request):
        print(request.POST('username'))
        return redirect('home')