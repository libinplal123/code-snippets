Step 6: Update the Django view to handle the form data and create a new user.

Update the register view in views.py to handle the form data and create a new user. Once the user is created, authenticate and log them in, and return a JSON response indicating success.

python
Copy code
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
