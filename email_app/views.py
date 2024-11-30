from django.shortcuts import render
from django.core.mail import send_mail
from .forms import EmailForm

def send_email(request):
    message = ""
    if request.method == "POST":
        form = EmailForm(request.POST)
        if form.is_valid():
            recipient = form.cleaned_data['recipient']
            subject = form.cleaned_data['subject']
            message_body = form.cleaned_data['message']
            try:
                send_mail(
                    subject,
                    message_body,
                    'from@example.com',  # Gönderen
                    [recipient],         # Alıcı
                )
                message = "Email sent successfully!"
            except Exception as e:
                message = f"Failed to send email: {e}"
    else:
        form = EmailForm()

    return render(request, 'email_app/email_form.html', {'form': form, 'message': message})
