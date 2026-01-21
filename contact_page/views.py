from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core.mail import send_mail
from .models import ContactMessage  
import json

@csrf_exempt
def contact_api(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        email = data.get('email')
        message = data.get('message')

        if not name or not email or not message:
            return JsonResponse({'error': 'All fields are required.'}, status=400)

        # Save to database
        ContactMessage.objects.create(
            name=name,
            email=email,
            message=message
        )

        full_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

        try:
            # Send to admin
            send_mail(
                subject='New Contact Form Message',
                message=full_message,
                from_email='akshayu1223@gmail.com',
                recipient_list=['akshayu1223@gmail.com'],
                fail_silently=False,
            )

            # Send acknowledgement to user
            send_mail(
                subject="Thank You for Contacting Us",
                message=f"Hi {name},\n\nThank you for reaching out! We have received your message and will get back to you shortly.\n\n— RIK Team",
                from_email='akshayu1223@gmail.com',
                recipient_list=[email],
                fail_silently=False,
            )

            return JsonResponse({'message': 'Message sent and saved successfully'}, status=200)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=100)

    return JsonResponse({'error': 'Invalid request'}, status=100)