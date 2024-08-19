from django.shortcuts import render, redirect
from .forms import StudentForm
from django.shortcuts import HttpResponse
from .models import Student


def view_register(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('')  # Redirect to a success page
    else:
        form = StudentForm()

    return render(request, 'register.html', {'form': form})