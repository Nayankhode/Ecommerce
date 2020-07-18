from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm

def home_page(request):
    context = {
        "title":"hello world",
        "content": "welcome to home page"

    }
    if request.user.is_authenticated():
        context["premium_content"] = "yeahhh"
    return render(request, "home_page.html", context)
def login_page(request):
    form =  LoginForm(request.POST or None)
    context = {
        "form": form
    }
    print(request.user.is_authenticated())
    if form.is_valid():
        print(form.cleaned_data)
        username =  form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user =  authenticate(request, username = username, password = password)
        print(request.user.is_authenticated())
        if user is not None:
            print(request.user.is_authenticated())
            login(request, user)
            context['form'] =  LoginForm()
            return redirect("/")
        else:
            print("error")

    return render(request, "auth/login.html", context)

User = get_user_model
def register_page(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        context = {
            "form": form}
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        new_user = User.objects.create_user(username,email,password)
        print(new_user)
    return render(request, "auth/register.html", {})