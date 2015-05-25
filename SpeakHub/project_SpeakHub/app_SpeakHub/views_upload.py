from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
# Decorator to use built-in authentication system
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from models import Audio
from forms import AudioForm
import os
import time

#@login_required
def upload(request):

    html= 'upload_audio.html'

    audio_to_add=Audio()
    
    if request.method=='GET':
        audioForm=AudioForm(instance=audio_to_add)
        return render_to_response(
         html,
         {'form': audioForm},
         context_instance=RequestContext(request)
         )

    audioForm=AudioForm(request.POST, request.FILES, instance=audio_to_add)
    
    if not audioForm.is_valid():
        return render_to_response(
         html,
         {'form': audioForm},
         context_instance=RequestContext(request)
         )

    audioForm.save()

    return redirect('home')

    