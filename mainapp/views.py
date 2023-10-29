from django.shortcuts import render


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Все получилось contacts: {name} {phone}: {message}')
    return render(request, 'mainapp/contacts.html')


def home(request):
    return render(request, 'mainapp/home.html')


