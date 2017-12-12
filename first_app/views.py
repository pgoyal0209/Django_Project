# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render , redirect , render_to_response
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import SignUpForm , DocumentForm
from .models import Document
from .filter import UserFilter
import os
from django.conf import settings
from django.template import RequestContext , context
from wsgiref.util import FileWrapper

def home(request):
    return render(request,'home.html')

def viewfiles(request):
    documents = Document.objects.all()

    return render(request,'viewfiles.html',{'documents':documents})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def myaccount(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES, request.user)
        if form.is_valid():
            document=form.save(commit=False)
            document.uploaded_by=request.user
            form.save()
            return redirect('viewfiles')
    else:
        form = DocumentForm()
    return render( request,'myaccount.html',
        {'form': form}
    )

def search(request):
    user_list = User.objects.all()
    user_filter = UserFilter(request.GET, queryset=user_list)
    return render(request, 'user_list.html', {'filter': user_filter})

def profile(request):
    user_list = User.objects.all()
    user_filter = UserFilter(request.GET, queryset=user_list)
    return render(request, 'profile.html', {'filter': user_filter})
