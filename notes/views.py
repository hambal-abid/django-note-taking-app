from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Notes
from .forms import NotesForm

# Create your views here.
def list_note(request):
    notes = Notes.objects.all()
    context = {
        'notes': notes
    }
    return render(request, 'index.html', context)

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

def delete_note(request, pk):
    note = get_object_or_404(Notes, pk=pk)
    note.delete()
    return redirect(reverse('list'))
