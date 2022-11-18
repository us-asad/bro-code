from django.shortcuts import render, redirect

# Create your views here.
from .models import Contact
from .forms import ContactForm


def sendMsg(request):
	form = ContactForm(request.POST or None)
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return redirect('post:index')
	return render(request, 'contact.html', {'form':form,})



# def contact(request):
# 	if request.method == 'POST':
# 		fullname = request.POST['fullname']
# 		email = request.POST['email_user']
# 		phone_num = request.POST['phone_num'] #WORKING but Wrong!!!
# 		body = request.POST['body']
# 		return render(request, 'contact.html', 
# 			{'fullname':fullname,
# 			'email_user':email,
# 			'phone_num':phone_num,
# 			'body':body,
# 			})
# 	else:
# 		return render(request, 'contact.html')