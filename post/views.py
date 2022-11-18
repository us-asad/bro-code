from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth import get_user_model

from .models import Post 
from .forms import PostForm

User = get_user_model()


def index(request):
	return render(request, 'index.html')

def postNew(request):
	form = PostForm(request.POST or None, request.FILES or None)
	if request.user.is_authenticated:
		author = User.objects.get(username=request.user)
	else:
		pass
	if request.method == 'POST':
		if form.is_valid():
			form.instance.author = author
			form.save()
			return redirect('post:postList')
	context={
	'form':form,
	}
	return render(request, 'post/postNew.html', context)


def postUpdate(request, id):
	title = 'Update'
	post = get_object_or_404(Post, id=id)
	form = PostForm(
		request.POST or None,
	 	request.FILES or None,
	 	instance=post)
	author = User(request.user)
	if request.method == 'POST':
		if form.is_valid():
			# form.instance.author = author
			form.save()
			return redirect('postList')
	context = {
	'form': form,
	'title': title
	}
	return render(request, 'post/postUpdate.html', context)

def postDetail(request, id):
	post = get_object_or_404(Post, id=id)
	return render(request, 'post/postDetail.html', {'post':post},)


def postList(request):
	posts = Post.objects.order_by('-timestamp')
	return render(request, 'postList.html', {'posts':posts,})


def postDel(request, id):
	post =  get_object_or_404(Post, id=id)
	post.delete()
	return redirect('post:postList')


def about(request):
	return render(request, 'about.html')

def team(request):
	return render(request, 'team.html') 

def service(request):
	return render(request, 'service.html')

def client(request):
	return render(request, 'client.html')