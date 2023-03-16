from django.shortcuts import render


# Create your views here.
# from django.http import HttpResponse
# from django.template import loader


def home(request):
    a = int(input("Сколько цифр мне нужно вывести?\n"
                  ""))
    numbers = ''
    for i in range(1, a + 1):
        numbers += f"{i} "

    return render(request, 'mainpage/index.html', context={'numbers': numbers})
