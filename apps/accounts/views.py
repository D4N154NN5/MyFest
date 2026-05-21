from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm
from apps.events.models import ShiftAssignment


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registrierung erfolgreich!")
            return redirect("dashboard")
    else:
        form = RegisterForm()
    return render(request, "accounts/register.html", {"form": form})


@login_required
def dashboard(request):
    assignments = ShiftAssignment.objects.filter(
        user=request.user
    ).select_related("shift__event").order_by("shift__start_time")
    return render(request, "accounts/dashboard.html", {"assignments": assignments})
