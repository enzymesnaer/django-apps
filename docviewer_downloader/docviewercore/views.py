from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, FileResponse, Http404
import os

# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('docviewercore:login')
    else:
        form = UserCreationForm()
    return render(request, 'docviewercore/signup.html', {'form':form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('docviewercore:home')
    else:
        form = AuthenticationForm()
    return render(request, 'docviewercore/login.html', {'form':form})


def logout_request(request):
    logout(request)
    return redirect("docviewercore:home")


def home_view(request):
    if request.method == 'POST':
        for count, x in enumerate(request.FILES.getlist("files")):
            def handle_uploaded_file(f):
                with open('media/'+ str(x), 'wb+') as destination:
                    for chunk in f.chunks():
                        destination.write(chunk)
            handle_uploaded_file(x)
        return HttpResponseRedirect("/filesuploaded/")
    messages.success(request, os.listdir('media'))
    return render(request, 'docviewercore/home.html')

def filesuploaded_view(request):
    messages.success(request, 'Upload Successful')
    return HttpResponseRedirect("/home/")


def file_viewer(request):
    if request.method == 'POST':
        filename = request.POST.get('filename')
        extn = os.path.splitext(filename)[1][1:]
        if extn in ['jpg','JPG','jpeg','JPEG','png','PNG']:
            try:
                return FileResponse(open('media/'+ filename, 'rb'))
            except FileNotFoundError:
                raise Http404('not found')
        if extn == 'pdf' or extn == 'PDF':
            try:
                return FileResponse(open('media/'+ filename, 'rb'), content_type='application/pdf')
            except FileNotFoundError:
                raise Http404('not found')
        if extn == 'docx' or extn == 'DOCX':
            try:
                return FileResponse(open('media/'+ filename, 'rb'))
            except FileNotFoundError:
                raise Http404('not found')
        if extn == 'pptx' or extn == 'PPTX':
            try:
                return FileResponse(open('media/'+ filename, 'rb'))
            except FileNotFoundError:
                raise Http404('not found')
        
def download(request):
    if request.method == 'GET':
        filename = request.GET.get('filename')
        response = HttpResponse(content_type='application/force-download') 
        response['Content-Disposition'] = f'attachment; filename={filename}'
        response['X-Sendfile'] = f'media/{filename}'
        return response
