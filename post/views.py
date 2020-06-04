from django.shortcuts import render,HttpResponse,get_object_or_404,HttpResponseRedirect,redirect
from .models import Post
from .forms import PostForm
from django.contrib import messages
from django.utils.text import slugify
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def post_index(request):
    contact_list = Post.objects.all()
    query = request.GET.get('q')
    if query:
        contact_list = contact_list.filter(
            Q(title__icontains=query) |
            Q(text__icontains=query) |
            Q(user__first_name__icontains=query) |
            Q(user__last_name__icontains=query)
        ).distinct()
    
    
    

    paginator = Paginator(contact_list,6 )

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)
    return render(request, 'index.html', {'posts': posts})
def hak(request):
    return render(request,'about.html')
def home(request):
    contact_list = Post.objects.all()
    query = request.GET.get('q')


    paginator = Paginator(contact_list,12 )

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)
    return render(request, 'home.html', {'posts': posts})


def post_detail(request,slug):
    post = get_object_or_404(Post,slug=slug)
    context={
        'post':post,
    }
    return render(request,'details.html',context)
    

def post_create(request):
    if not request.user.is_authenticated:
        return Http404

    form = PostForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.user=request.user
        post.save()
        messages.success(request, 'başarılı bir şekilde oluşturdunuz')
        return HttpResponseRedirect(post.get_absolute_url())
    context = {
        'form': form,
    }
    return render(request,'form.html',context)


def post_update(request,slug):
    if not request.user.is_authenticated:
        return Http404
    post = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None,request.FILES or None,instance=post)
    if form.is_valid():
        form.save()

        messages.success(request, 'Başarılı bir şekilde oluşturdunuz')
        return HttpResponseRedirect(post.get_absolute_url())
    context = {
        'form': form,
    }
    return render(request, 'form.html', context)



def post_detele(request,slug):
    if not request.user.is_authenticated:
        return Http404
    post = get_object_or_404(Post, slug=slug)
    post.delete()
    return redirect('post:index')

    