from django.shortcuts import render
from .models import User
from django.contrib import messages
# Create your views here.
def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password :
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists')
                return render(request, 'register.html')
            elif User.objects.filter(phone=phone).exists():
                messages.info(request, 'Phone number already exists')
                return render(request, 'register.html')
            else:
                user = User.objects.create_user(email=email, phone=phone, password=password)
                user.save()
                messages.success(request, 'Registration successful')
                return render(request, 'login.html')
