from django.shortcuts import render
from django.http import HttpResponse
from .models import ContactMessage
from .utils import notify


def contact(request):
    if request.method == 'POST':
        # Handle the form submission
        # Extract form data from request.POST dictionary
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Create a new ContactMessage object
        contact_message = ContactMessage(name=name, email=email, message=message)
        contact_message.save()

        # Send email
        notify(name, email, message)

        # Return a success message
        return render(request, 'about/about.html', {'show_modal': True})
    else:
        # Render the contact form
        return render(request, 'about/about.html')
