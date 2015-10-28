from django.shortcuts import get_object_or_404,render
from branch.forms import data, UserForm
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.context_processors import csrf
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import Document
from .forms import DocumentForm
# Create your views here.



def register(request):
	registered = False
	if request.method == 'POST':
		user_form = UserForm(request.POST)
		if user_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()
			registered = True
			return render(request,'register.html',{'user_form': user_form, 'registered': registered} )
		else:
			return render(request,'register.html',{'user_form': user_form, 'registered': registered} )
	else:
		user_form = UserForm()
		return render(request,'register.html',{'user_form': user_form, 'registered': registered} )
def user_login(request):
	wrong_credentials = False
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('form')
			else:
				return HttpResponse("Your Rango account is disabled.")
		else:
			wrong_credentials = True
			return render(request, 'login.html', {'wrong_credentials': wrong_credentials})
	else:
		return render(request, 'login.html', {'wrong_credentials': wrong_credentials})


@login_required
def user_logout(request):
    logout(request)

    return HttpResponseRedirect('login')

@login_required
def formdisplay(request):
	print("3")
	if request.method == 'POST':
		form = data(request.POST)
		print("2")
		if form.is_valid():
			user = request.user
			profile = form.save(commit=False)
			profile.user = user
			profile.save()
			print("1")
			
			return HttpResponseRedirect('hello')
		else:
			print("4")
			return render(request, 'UI.html', {'form': form})
	else:
		print("5")
		form = data()
		return render(request, 'UI.html', {'form': form})



def lists(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('branch.views.lists'))
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'branch/list.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )