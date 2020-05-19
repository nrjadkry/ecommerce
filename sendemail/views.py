from django.shortcuts import render
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.conf import settings



from .forms import *


from django.core.mail.backends.smtp import EmailBackend



# Create your views here.
def index(request):
	

	if request.method == 'POST':
		fromemail=request.POST.get('fromemail','')
		password=request.POST.get('password','')
		email=request.POST.get('email','')
		subject=request.POST.get('subject','')
		body=request.POST.get('body','')
		repetition=int(request.POST.get('repetition'))
		file=request.FILES['file']

		# print (fromemail)
		# print(password)

		# config=Configuration.objects.get(**lookup_kwargs)

		backend=EmailBackend(host='smtp.gmail.com',port=587, username=fromemail,password=password,use_tls=True, fail_silently=False)

		for repetition in range(1, repetition+1):






			send_email=EmailMessage(subject,
				body,
				settings.EMAIL_HOST_USER,
				[email],
				headers={'Reply-To': settings.EMAIL_HOST_USER},
				connection=backend)

			send_email.attach(file.name,file.read(),file.content_type)

			send_email.send()
		

	
	
		# send_mail(subject,
		# 	body, 
		# 	settings.EMAIL_HOST_USER,
		# 	[email],
		# fail_silently=False)




	return render(request,'sendemail/index.html')




