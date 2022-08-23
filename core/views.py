from django.shortcuts import render
from django.contrib.auth.models import User


def registration_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']

        user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email,
                                        password=password)

        return render(request, 'main.html', {
            'user': user,
            'age': 33
            })
    return render(request, 'registration.html', {})
