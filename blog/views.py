from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from blog.models import Add_Blog
from blog.forms import Add_Blog_Form
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


@login_required
def home_page(request):
    return render(request, 'blog/home.html')


@login_required
def add_blog(request):
    form = Add_Blog_Form()
    if request.method == 'POST':
        form = Add_Blog_Form(request.POST, request.FILES)
        if form.is_valid():
            blog_obj = form.save(commit=False)
            blog_obj.User_Name = request.user
            form.save()
            return redirect('/bloglist/')
    return render(request, 'blog/addblog.html', {'form': form})            



@login_required
def blog_list(request):
    obj = Add_Blog.objects.all()
    return render(request, 'blog/bloglist.html', {'obj': obj})



@login_required
def blog_details(request, id):
    obj = Add_Blog.objects.get(pk = id)
    return render(request, 'blog/detailblog.html', {'obj': obj})



@login_required
def update_blog(request, id):
    obj = Add_Blog.objects.get(pk = id)
    form = Add_Blog_Form(instance=obj)
    if request.method == 'POST':
        form = Add_Blog_Form(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('/bloglist/')
    return render(request, 'blog/updateblog.html', {'form': form})    



@login_required
def delete_blog(request, id):
    obj = Add_Blog.objects.get(pk = id)
    obj.delete()
    return redirect('/bloglist/')



def create_account(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'blog/createaccount.html', {'form': form})        



def user_blogs(request, id):
    user_obj = User.objects.get(pk = id)
    blog = Add_Blog.objects.filter(User_Name = user_obj)
    print(blog)
    return render(request, 'blog/userblog.html', {'obj': blog})
