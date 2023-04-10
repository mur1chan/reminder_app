from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Reminder
from .forms import AddReminder
# Create your views here.
def index(request):
    collect_reminder = Reminder.objects.all()
    return render(request, 'index.html', {'collect_reminder':collect_reminder})

def add_reminder(request):
    if request.POST:
        form = AddReminder(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
        return redirect(add_reminder)
    return render(request, "add_reminder.html", {'form':AddReminder})

def delete_reminder(request):
    return HttpResponse("this is the delete response")