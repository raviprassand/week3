from django.shortcuts import render, redirect
from .forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signup_success')  # Redirect to a success page
    else:
        form = SignUpForm()
    return render(request, 'useraccounts/signup.html', {'form': form})


def home(request):
    return render(request, 'useraccounts/home.html')

