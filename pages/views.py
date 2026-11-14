from django.shortcuts import render


def home(request):
    context = {
        'name': 'Ibraheem',
        'role': 'BS Software Engineering student',
    }
    return render(request, 'pages/home.html', context)


def about(request):
    return render(request, 'pages/about.html')


def projects(request):
    return render(request, 'pages/projects.html')


def contact(request):
    context = {'email': 'ibrahimnaveed00@gmail.com'}
    return render(request, 'pages/contact.html', context)
