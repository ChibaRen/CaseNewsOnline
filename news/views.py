from django.shortcuts import render, redirect
from django.utils import timezone
from .forms import InputForm
from .models import InputModelForm

# Create your views here.
def index(request):
    form = InputForm(request.POST or None)
    if form.is_valid():
        case = InputModelForm()
        case.name = form.cleaned_data['name']
        case.age = form.cleaned_data['age']
        case.mail = form.cleaned_data['mail']
        case.title = form.cleaned_data['title']
        case.history = form.cleaned_data['history']
        case.done = form.cleaned_data['done']
        case.question = form.cleaned_data['question']
        case.idea = form.cleaned_data['idea']
        case.reference = form.cleaned_data['reference']
        case.save()

        InputModelForm.objects.create(
            name = case.name,
            age = case.age,
            mail = case.mail,
            title = case.title,
            history = case.history,
            done = case.done,
            question = case.question,
            idea = case.idea,
            reference = case.reference,
            created_at = timezone.now,
        )
        #return redirect('list')
    return render(request, 'index.html', {'form':form})

def listfunc(request):
    posts = InputModelForm.objects.all()
    return render(request, 'list.html', {'post':posts})