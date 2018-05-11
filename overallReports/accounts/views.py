# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
    )
from .forms import UserLoginForm, UserRegisterForm
from posts.models import Post


def login_view(request):
    queryset = Post.objects.all()
    next = request.GET.get("next")
    title = "Login"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect("/")

    context = {
        "object_list": queryset,
        "form": form,
        "title": title,
        "caption": "New User ?",
        "link": "Register Here",
        "account": "register",
    }

    return render(request, "form.html", context)


def register_view(request):
    next = request.GET.get("next")
    queryset = Post.objects.all()
    title = "Register"
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect("/")

    context = {
        "object_list": queryset,
        "form": form,
        "title": title,
        "caption": "Got an account ?",
        "link": "Login Here",
        "account": "login",
    }

    return render(request, "form.html", context)


def logout_view(request):
    logout(request)
    return redirect("/")
