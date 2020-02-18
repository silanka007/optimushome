from django.shortcuts import render


def homePage(request):
    return render(request, 'pages/index.html')


def aboutPage(request):
    return render(request, 'pages/about.html')
