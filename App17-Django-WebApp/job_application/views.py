from django.core.mail import EmailMessage
from django.shortcuts import render
from .forms import ApplicationForm
from .models import Form
from django.contrib import messages

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            date = request.POST['date']
            occupation = request.POST['occupation']

            Form.objects.create(first_name=first_name, last_name=last_name, email=email,
                                date=date, occupation=occupation)

            #messages_body = f"A new Job Application was submitted. Thank you for applying! {first_name} {last_name}"
            #email_message = EmailMessage("Form Submission Confirmation", messages_body, to=[email])
            #email_message.send()

            messages.success(request, 'Form submitted successfully!')
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')