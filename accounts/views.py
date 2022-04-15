from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import AccountAddForm
from django.contrib.auth import get_user_model

def signup(request):
  if request.method == 'GET':
    form = AccountAddForm
  elif request.method == 'POST':
    form = AccountAddForm(request.POST)
    if form.is_valid():
        get_user_model().objects.create_user(
            username=form.cleaned_data['username'],
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password']
        )
        return redirect('../login')
  context = {
    'form': form
  }
  return render(request, 'registration/signup.html', context)
