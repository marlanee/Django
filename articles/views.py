from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        'name': '이정원',
        'topic': 'python',
        'study_day': 5,
        'topics': ['Python', 'HTML', 'Django', 'Codex'],
    }
    return render(request, 'articles/index.html', context)

def hello(request):
    context = {
        'nickname': '가든',
        'goal': 'AI 계급사회',
        'goals': ['Algo_B', 'Ai_skills', 'Backend'],
    }
    return render(request, 'articles/hello.html', context)

def throw(request):
    return render(request, 'articles/throw.html')

def study_time(request):
    return render(request, 'articles/study_time.html')

def catch(request):
    message = request.GET.get('message', '')

    context = {
        'message': message,
    }
    return render(request, 'articles/catch.html', context)

def study_catch(request):
    message = request.GET.get('message', '')

    context = {
        'message': message,
    }
    return render(request, 'articles/study_catch.html', context)