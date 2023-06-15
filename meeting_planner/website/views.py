from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render
from meetings.models import Meeting, Room


def welcome(request):
    return render(request, "website/welcome.html", {"meetings": Meeting.objects.all()})


def date(request):
    return HttpResponse("This page was called at " + str(datetime.now()))


def about(request):
    return HttpResponse("About myself, software engineer with 20+ years experience")
