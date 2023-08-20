from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login, logout, authenticate
from .models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import CustomUserCreationForm, UserLoginForm, UserUpdateForm
from django.contrib.auth.forms import AuthenticationForm

from django.http import HttpResponseRedirect
from django.urls import reverse

from .decorators import user_not_authenticated






@login_required
def custom_logout(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("/")


@user_not_authenticated
def custom_login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(
                email=form.cleaned_data["email"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                messages.success(request, f"Hello {user.email}! You have been logged in")
                return redirect("/")

        else:
            for error in list(form.errors.values()):
                messages.error(request, error) 

    form = UserLoginForm()

    return render(
        request=request,
        template_name="auth/login.html",
        context={"form": form}
        )

def register(request):
    # Logged in user can't register a new account
    if request.user.is_authenticated:
        return redirect("/")

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
        else:
            for error in list(form.errors.values()):
                print(request, error)

    else:
        form = CustomUserCreationForm()

    return render(
        request = request,
        template_name = "register.html",
        context={"form":form}
        )

def profile(request, email):
    if request.method == "POST":
        user = request.user
        form = UserUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            user_form = form.save()
            messages.success(request, f'{user_form.email}, Your profile has been updated!')
            return redirect("profile", user_form.email)

        for error in list(form.errors.values()):
            messages.error(request, error)

    user = User.objects.filter(email=email).first()
    if user:
        form = UserUpdateForm(instance=user)
        # form.fields['first_name'].widget.attrs = {'rows': 1}
        return render(
            request=request,
            template_name="auth/profile.html",
            context={"form": form}
            )
    
    return redirect("homepage")


# def followToggle(request, author):
#         authorObj = CustomUser.objects.get(username=author)
#         currentUserObj = CustomUser.objects.get(username=request.user.email)
#         following = authorObj.following.all()

#         if author != currentUserObj.email:
#             if currentUserObj in following:
#                 authorObj.following.remove(currentUserObj.id)
#             else:
#                 authorObj.following.add(currentUserObj.id)

#         return HttpResponseRedirect(reverse(profile, args=[authorObj.email]))