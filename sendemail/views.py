from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.conf import settings
from django.http import HttpResponse
from django.contrib import messages




from .forms import EmailForm


from django.core.mail.backends.smtp import EmailBackend



# Create your views here.
def index(request):
	

	if request.method == 'POST':
		form=EmailForm(request.POST)
		if form.is_valid:

			fromemail=request.POST.get('fromemail','')
			password=request.POST.get('password','')
			email=request.POST.get('email','')
			bcc=request.POST.get('bcc','')
			cc=request.POST.get('cc','')
			subject=request.POST.get('subject','')
			body=request.POST.get('body','')
			repeat=request.POST.get('repetition','')
			file=request.FILES.get('file',False)

			# repetition=int(repeat)
			# doc=request.FILES
			# file=doc['file']

			if not fromemail or not password or not email:
				# print('Error here')
				messages.info(request, 'Enter all the credentials')

			else:
				if not repeat:
					repetition=1
				else:
					repetition=int(repeat)





				if not body and not file:
					# raise ValidationError ("You must use either body or attachment section.")
					messages.info(request, 'Enter the content of email')


				else:




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

							if file:
								print ('FIle')

								send_email.attach(file.name,file.read(),file.content_type)

							send_email.send()
							messages.success(request, 'Email was sent at ' + email)
							return redirect('/sendemail')

					except:
						
						messages.info(request, 'Your Email or password is incorrect.')
						
	else:
		form=EmailForm()
		print("error")
	
	# AuthenticationError
	
		# send_mail(subject,
		# 	body, 
		# 	settings.EMAIL_HOST_USER,
		# 	[email],
		# fail_silently=False)




	return render(request,'sendemail/index.html',{'form':form})




