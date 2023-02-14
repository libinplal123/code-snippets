from django.shortcuts import render, redirect
from .models import Contact

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        Contact.objects.create(name=name, email=email, message=message)
        return redirect('success')

    contacts = Contact.objects.all()
    return render(request, 'myapp/contact.html', {'contacts': contacts})

def success(request):
    contacts = Contact.objects.all()
    return render(request, 'myapp/success.html', {'contacts': contacts})
