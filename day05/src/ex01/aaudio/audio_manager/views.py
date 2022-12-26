from django.shortcuts import render
from django.http import HttpResponse
import pathlib
import os

#safety
from html import escape

# upload form
from .forms import AudioUploadForm


def test(request):
    errors = 0
    if request.method == "POST":
        oldform = AudioUploadForm(request.POST, request.FILES)
        if oldform.is_valid():
            file_handler(request.FILES['file'])
        else:
            errors = 1
    files = pathlib.Path.cwd().joinpath('static', 'audios')
    files = os.listdir(files)
    form = oldform if errors else AudioUploadForm()
    errors = 0
    return render(request,
                "audio_manager/index.html",
                {"files": files, "form": form})
# Create your views here.


def file_handler(file):
    name = escape(file.name)
    with open('static/audios/' + name, "wb+") as dest:
        for chunk in file.chunks():
            dest.write(chunk)

