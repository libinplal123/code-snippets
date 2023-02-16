from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # create the new user
        user = User.objects.create_user(username, email, password)
        user.save()
        
        # authenticate and log in the user
        user = authenticate(username=username, password=password)
        login(request, user)
        
        return JsonResponse({'success': True})
    
    return render(request, 'registration/register.html')
