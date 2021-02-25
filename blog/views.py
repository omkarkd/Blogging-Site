from django.shortcuts import render
from django.http import HttpResponse


posts = [
    {
        'author':'omkar kadam',
        'title':'blog post 1',
        'content':'first blog post',
        'date_posted':'sept 2021'
    },
    {
        'author':'krishna gandi',
        'title':'blog post 2',
        'content':'Second blog post',
        'date_posted':'oct 2021'
    }
]


def home(request):
    context = {'posts':posts}

    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{'title':'About'})
