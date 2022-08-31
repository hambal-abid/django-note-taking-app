from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.contrib import messages
from .models import Notes
from .forms import NotesForm
from signup import urls

# Create your views here.
@login_required(login_url='start') #restricts direct access to the main page using url without login credentials
@cache_control(no_cache=True, must_revalidate=True, no_store=True) #prevents back-tracking to the previous page
def list_note(request):
    notes = Notes.objects.all()
    context = {
        'notes': notes
    }
    return render(request, 'index.html', context)

@login_required(login_url='start')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def add_note(request):
    if request.method == 'POST':
        form = NotesForm(request.POST or None)
        if form.is_valid():
            t = request.POST['title']
            b = request.POST['body']
            note = Notes(title=t, body=b)
            note.save()
            return redirect(reverse('list'))
    return render(request, 'addModal.html', {})

@login_required(login_url='start')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def edit_note(request, pk):
    editnote = get_object_or_404(Notes, pk=pk)
    if request.method == 'POST':
        form = NotesForm(request.POST or None)
        if form.is_valid():
            editnote.title = request.POST['title']
            editnote.body = request.POST['body']
            editnote.save()
            return redirect(reverse('list'))
    context = {
        'editnote' : editnote
    }
    return render(request, 'editModal.html', context)

@login_required(login_url='start')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def delete_note(request, pk):
    note = get_object_or_404(Notes, pk=pk)
    note.delete()
    return redirect(reverse('list'))
