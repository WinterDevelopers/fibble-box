from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.text import slugify

from .models import Writer, Post, Comment
from .forms import CommentForm, PostForm, WriterForm

from django.http import HttpResponse

def about(request):
    return HttpResponse('about page')

# Create your views here.
def index(request):
    template_name = "blog.html"
    return render(request, template_name)


@login_required(login_url="/pageantry/login/")
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
    template_name = "posts_list.html"
    context = {"posts": posts}
    return render(request, template_name, context)


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    post.insight = (post.insight+1)
    post.save()
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
    comments = post.comment_set.all()
    other_posts = Post.objects.all()[:3]
    template_name = "post_detail.html"
    context = {"post": post, "form": form, "comments": comments, 'other_posts':other_posts}
    return render(request, template_name, context)


@login_required(login_url="/pageantry/login/")
def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            writer = get_object_or_404(Writer, user=request.user)
            new_post.writer = writer
            new_post.slug = slugify(new_post.title)
            new_post.save()
            return redirect(new_post.get_absolute_url())
    else:
        form = PostForm()
        if hasattr(request.user, "writer"):
            writer = request.user
        else:
            print("u are not a writer.")
    template_name = "add_post.html"
    context = {"form": form}
    return render(request, template_name, context)


@login_required(login_url="/pageantry/login/")
def edit_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.user == post.writer:
        if request.method == "POST":
            form = PostForm(instance=post, data=request.POST)
            if form.is_valid():
                updated_post = form.save(commit=False)
                updated_post.slug = slugify(updated_post.title)
                updated_post.save()
                return redirect(post.get_absolute_url())
        else:
            form = PostForm(instance=post)
    else:
        return HttpResponseForbidden()
    template_name = "edit_post.html"
    context = {"form": form}
    return render(request, template_name, context)


@login_required(login_url="/pageantry/login/")
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
    