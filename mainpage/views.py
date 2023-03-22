from django.shortcuts import render


# Create your views here.
# from django.http import HttpResponse
# from django.template import loader


def home(request):
    name = 'bob'

    return render(request, 'mainpage/index.html', context={'numbers': name})


def about(request):
    name = 'about us'

    return render(request, 'mainpage/about.html', context={'numbers': name})
