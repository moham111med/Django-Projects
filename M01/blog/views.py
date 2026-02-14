from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404
from .models import Post 
# Create your views here.

# def home(request):
#     return HttpResponse('<center><h1>Home Page</h1></center>')

# def about(request):
#     return HttpResponse('<center><h1>About Page</h1></center>')

#!ولكن الافضل ان نرجع templete كامل وليس مجرد tags عادي
#1. نعمل ملجد اسمه template
#2.نضع فيه اكواد html ونسميه بنفس اسم الدالة
#*we use function(render) and it returns HttpResponse too
def home(request):
    return render(request,'home.html')
#يمكنك كتابة المسار بدون templates لانه يبحث هناك تلقائياً
def about(request):
    return render(request,'about.html')
#!new
def post_list(request):
    posts=Post.objects.all()
    return render(request,'blog/post/list.html',{'posts':posts})
def post_detail(request,id):
    #*method1
    # try:
    #     post=Post.objects.get(id=id)
    # except Post.DoesNotExist:
    #     raise Http404('No Post Found')
    # return render (request,'blog/post/detail.html',{'post':post})
    
    #*method2
    post=get_object_or_404(Post,id=id,status=Post.Status.PUBLISHED)
    return render (request,'blog/post/detail.html',{'post':post})
    