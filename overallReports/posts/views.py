# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponseRedirect, Http404
from django.contrib.contenttypes.fields import ContentType
from django.contrib import messages
from django.shortcuts import render
from django.utils import timezone
from django.db.models import Q
from urllib import quote_plus
from .forms import PostForm
from .models import Post
from comments.forms import CommentForm
from comments.models import Comment


def post_detail(request, slug=None):
    instance = get_object_or_404(Post, slug=slug)
    if instance.draft or instance.publish > timezone.now().date():
        if not request.user.is_staff or not request.user.is_superuser:
            raise Http404
    share_string = quote_plus(instance.content)
    queryset = Post.objects.all()

    initial_data = {
        "content_type": instance.get_content_type,
        "object_id": instance.id,
    }
    form = CommentForm(request.POST or None, initial=initial_data)
    if form.is_valid() and request.user.is_authenticated():
        c_type = form.cleaned_data.get("content_type")
        content_type = ContentType.objects.get(model=c_type)
        obj_id = form.cleaned_data.get("object_id")
        content_data = form.cleaned_data.get("content")
        parent_obj = None

        try:
            parent_id = int(request.POST.get("parent_id"))
        except:
            parent_id = None

        if parent_id:
            parent_qs = Comment.objects.filter(id=parent_id)
            if parent_qs.exists() and parent_qs.count() == 1:
                parent_obj = parent_qs.first()

        new_comment, created = Comment.objects.get_or_create(
                                user=request.user,
                                content_type=content_type,
                                object_id=obj_id,
                                content=content_data,
                                parent=parent_obj)
        return HttpResponseRedirect(new_comment.content_object.get_absolute_url())

    comments = instance.comments
    context = {
        "object_list":queryset,
        "title": instance.title,
        "instance": instance,
        "share_string": share_string,
        "comments": comments,
        "comment_form": form,
    }
    return render(request, "post_detail.html", context)


def post_list(request):
    today = timezone.now().date()
    queryset_list = Post.objects.active()
    if request.user.is_staff or request.user.is_superuser:
        queryset_list = Post.objects.all()

    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(user__first_name__icontains=query) |
            Q(user__last_name__icontains=query)
            ).distinct()

    paginator = Paginator(queryset_list, 10)     # Show 5 POSTS per page
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    context = {
        "object_list":queryset,
        "title": "Welcome to Overall Reports",
        "page_request_var": page_request_var,
        "today": today,
    }
    return render(request, "post_list.html", context)


def post_create(request):
    queryset = Post.objects.all()
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        # Success Message
        messages.success(request, "Successfully Created.")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "object_list": queryset,
        "form": form,
    }
    return render(request, "post_form.html", context)


def post_update(request, slug=None):
    queryset = Post.objects.all()
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        # Success Message
        messages.success(request,"Successfully Updated.")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "object_list": queryset,
        "title": instance.title,
        "instance": instance,
        "form": form,
    }
    return render(request, "post_form.html", context)


def post_delete(request, slug=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post, slug=slug)
    # form = PostForm(request.POST or None, request.FILES or None, instance=instance)
    instance.delete()
    messages.success(request,"Successfully Deleted")
    return redirect("posts:list")
