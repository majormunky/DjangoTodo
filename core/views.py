from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import forms


def register_user(request):
    if request.method == "POST":
        form = forms.CoreUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = forms.CoreUserCreationForm()

    return render(request, "core/register-user.html", {"form": form})
