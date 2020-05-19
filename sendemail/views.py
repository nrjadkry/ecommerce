from django.shortcuts import render
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.conf import settings
from django.http import HttpResponse


from .forms import *


from django.core.mail.backends.smtp import EmailBackend



# Create your views here.
def index(request):
	

	if request.method == 'POST':
		fromemail=request.POST.get('fromemail','')
		password=request.POST.get('password','')
		email=request.POST.get('email','')
		bcc=request.POST.get('bcc','')
		cc=request.POST.get('cc','')
		subject=request.POST.get('subject','')
		body=request.POST.get('body','')
		repetition=int(request.POST.get('repetition'))
		file=request.FILES['file']




		# config=Configuration.objects.get(**lookup_kwargs)
		try:
		
			backend=EmailBackend(host='smtp.gmail.com',port=587, username=fromemail,password=password,use_tls=True, fail_silently=False)

			for repetition in range(1, repetition+1):






				send_email=EmailMessage(subject,
					body,
					settings.EMAIL_HOST_USER,
					[email],
					bcc=[bcc],
					cc= [cc],
					headers={'Reply-To': settings.EMAIL_HOST_USER},
					connection=backend)

				send_email.attach(file.name,file.read(),file.content_type)

				send_email.send()
		except:
			print('error')
			return HttpResponse('Your Email or password is incorrect.')

	
	# AuthenticationError
	
		# send_mail(subject,
		# 	body, 
		# 	settings.EMAIL_HOST_USER,
		# 	[email],
		# fail_silently=False)




	return render(request,'sendemail/index.html')




