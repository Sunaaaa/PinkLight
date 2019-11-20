from django.shortcuts import render, redirect, get_object_or_404
from .models import Train
from django import forms
from .forms import TrainForm


# Create your views here.
def index(request):
    trains = Train.objects.all()
    context = {
        'trains' : trains,
    }
    return render(request, 'webserver/index.html', context)

def new(request):

    if request.method == "POST":
        form = TrainForm(request.POST)
        print("뿜뿜")
        if form.is_valid():

            train_no = form.cleaned_data.get('train_no')
            print(train_no)
            slot_no = form.cleaned_data.get('slot_no')
            seat_no = form.cleaned_data.get('seat_no')
            train = Train.objects.create(train_no=train_no, slot_no=slot_no, seat_no=seat_no, empty="False")
        
        return redirect('webserver:index')
    else:
        form = TrainForm()

    context = {
        'form' : form ,
    }

    return render(request, 'webserver/form.html', context)


def detail(request, train_pk):
    train = get_object_or_404(Train, pk=train_pk)
    context = {
        'train' : train,
    }
    return render(request, 'webserver/detail.html', context)


def edit(request, train_pk):
    train = get_object_or_404(Train, pk=train_pk)
    if request.method == "POST":
        form = TrainForm(request.POST, instance=train)
        print("뿜뿜")
        if form.is_valid():
            train = form.save()
            return redirect('webserver:index', train_pk)
        
    else:
        form = TrainForm(instance=train)

    context = {
        'form' : form ,
    }

    return render(request, 'webserver/form.html', context)
