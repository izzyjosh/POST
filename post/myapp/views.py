from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Posts, Comment
from .forms import PostForm


def index(request):
	if not request.user.is_authenticated:
		return redirect("signin")
	posts = Posts.objects.filter(p_owner=request.user)
	
	return render(request, "index.html", {"posts":posts})
	
def signup(request):
	if request.user.is_authenticated:
		return redirect("index")
	if request.method == "POST":
		username = request.POST.get("username")
		email = request.POST.get("email")
		password1 = request.POST.get("password1")
		password2 = request.POST.get("password2")
		
		if password1 == password2:
			if User.objects.filter(username=username).exists():
				messages.error(request, "the username already exist")
				return redirect("signup")
			elif User.objects.filter(email=email).exists():
				messages.error(request, "the email already exist")
				return redirect("signup")
			else:
				User.objects.create_user(username=username, email=email, password=password1)
				
				messages.info(request, f"account for {username} created successfully")
			return redirect("signin")
		else:
			messages.error(request, "the passwords donot match")
	return render(request, "signup.html")
	
	
	
def signin(request):
	if request.user.is_authenticated:
		return redirect("index")
	if request.method == "POST":
		username = request.POST.get("username")
		password1 = request.POST.get("password1")
		
		user = auth.authenticate(username=username, password=password1)
		if user is not None:
			auth.login(request, user)
			messages.info(request, "signed in successfully")
			return redirect("index")
		else:
			messages.error(request, "incorrect password or username")
			return redirect("signin")
			
		
	return render(request, "signin.html")
	
def post(request):
	
	if request.method == "POST":
		post = request.POST.get("post")
		
		
		Posts.objects.create(post=post, p_owner=request.user)
		return redirect("index")
	
	return render(request, "post.html")
	
	
def l_comment(request, p_id):
	post = Posts.objects.get(id=p_id)
	if request.method == "POST":
		comment = request.POST.get("comment")
		
		Comment.objects.create(comment=comment, c_owner=post)
		
		return redirect("index")
	
	
	return render(request, "comment.html", {"post":post})


def view_comment(request, po_id):
	post = Posts.objects.get(id=po_id)
	comment = Comment.objects.filter(c_owner=post)
	return render(request, "view_comment.html", {"comment":comment})
	
	
def delete(request, post_id):
	post = Posts.objects.get(id=post_id)
	post.delete()
	return redirect("index")
	
def delete_c(request, com_id):
	comm = Comment.objects.get(id=com_id)
	comm.delete()
	return redirect("index")
	
	
def confirm(request, p_id):
	post = Posts.objects.get(id=p_id)
	return render(request, "confirm.html", {"post":post})
	
	
def update(request, po_id):
	post = Posts.objects.get(id=po_id)
	form = PostForm(request.POST or None, instance=post)
	
	if form.is_valid():
		form.save()
		return redirect("index")
	return render(request, "djform.html", {"form":form})
	
def update_c(request, c_id):
	comment = Comment.objects.get(id=c_id)
	form = PostForm(request.POST or None, instance=comment)
	
	if form.is_valid():
		form.save()
		return redirect("index")
	return render(request, "djform.html", {"form":form})
	
def logout(request):
	auth.logout(request)
	return redirect("signin")