from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.text import slugify

from .models import Writer, Post, Comment
from .forms import CommentForm, AddPostForm, EditPostForm, WriterForm


# Create your views here.
def index(request):
    template_name = "blog.html"
    return render(request, template_name)


@login_required(login_url="/pageantry/login/account/")
def become_writer(request):
    if request.method == "POST":
        form = WriterForm(request.POST)
        if form.is_valid():
            new_writer = form.save(commit=False)
            new_writer.user = request.user
            new_writer.save()
            return redirect("/")
    else:
        form = WriterForm()
    template_name = "become_writer.html"
    context = {"form": form}
    return render(request, template_name, context)


def posts_list(request):
    posts = Post.objects.all()
    template_name = "home.html"
    context = {"posts": posts}
    return render(request, template_name, context)


def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            comment = form.cleaned_data["comment"]
            new_comment = Comment(post=post, username=username, comment=comment)
            new_comment.save()
            return redirect(post.get_absolute_url())
        else:
            messages.error(request, "Your comment was not posted. Try again.")
            form.error_class
    else:
        form = CommentForm()
    comments = Comment.objects.all()
    template_name = "post_detail.html"
    context = {"post": post, "form": form, "comments": comments}
    return render(request, template_name, context)


@login_required(login_url="/pageantry/login/account/")
def add_post(request):
    if request.method == "POST":
        form = AddPostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            text = form.cleaned_data["text"]
            slug = slugify(title)
            writer = get_object_or_404(Writer, user=request.user)
            post = Post(title=title, text=text, slug=slug, writer=writer)
            post.save()
            return redirect(post.get_absolute_url())
    else:
        form = AddPostForm()
        if hasattr(request.user, "writer"):
            writer = request.user
        else:
            print("u are not a writer.")
    template_name = "add_post.html"
    context = {"form": form}
    return render(request, template_name, context)


@login_required(login_url="/pageantry/login/account/")
def edit_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.user == post.writer:
        if request.method == "POST":
            form = EditPostForm(instance=post, data=request.POST)
            if form.is_valid():
                title = form.cleaned_data["title"]
                text = form.cleaned_data["text"]
                slug = slugify(title)
                post = Post(title=title, text=text, slug=slug)
                post.save()
                return redirect(post.get_absolute_url())
        else:
            form = EditPostForm(instance=post)
    else:
        return HttpResponseForbidden()
    template_name = "edit_post.html"
    context = {"form": form}
    return render(request, template_name, context)


@login_required(login_url="/pageantry/login/account/")
def delete_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.user == post.writer:
        if request.method == "POST":
            post.delete()
            return redirect("/")
    else:
        return HttpResponseForbidden()
    template_name = "delete_post.html"
    context = {"post": post}
    return render(request, template_name, context)