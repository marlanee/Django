from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        'name': '이정원',
        'topic': 'python',
        'study_day': 5,
    }
    return render(request, 'articles/index.html', context)

def hello(request):
    context = {
        'nickname': '가든',
        'goal': 'AI 계급사회',
    }
    return render(request, 'articles/hello.html', context)


