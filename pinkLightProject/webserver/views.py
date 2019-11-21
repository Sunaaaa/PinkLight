from django.shortcuts import render, redirect, get_object_or_404
from .models import Train
from django import forms
from .forms import TrainForm
from django.http import JsonResponse
from django.db.models import Count
import requests

def station_status(request, station):
    print('뿜뿜뿜')
    print(type(station))
    # station_status = request.get(f'http://swopenapi.seoul.go.kr/api/subway/674d6171516d696e3432724143445a/json/realtimeStationArrival/0/5/{station}').json
    station_status = requests.get(f'http://swopenapi.seoul.go.kr/api/subway/674d6171516d696e3432724143445a/json/realtimeStationArrival/0/5/{station}').json()
    print(type(station_status))
    # print(station_status[realtimeArrivalList])
    data = station_status['realtimeArrivalList']
    print(len(data))
    context = {
        'one' : data[0],
        'two' : data[1],
    }
    return JsonResponse(context)


def station_info(request, train_name):
    print(train_name)
    context = {
        '상행' : [
            {
                '001002': [{
                    'slot_no' : '004',
                    'seat_no' : '01',
                    'empty' : False
                }, {
                    'slot_no' : '004',
                    'seat_no' : '02',                    
                    'empty' : False
                }, {
                    'slot_no' : '004',
                    'seat_no' : '03',                    
                    'empty' : False
                }, {
                    'slot_no' : '005',
                    'seat_no' : '01',                    
                    'empty' : False
                }, {
                    'slot_no' : '005',
                    'seat_no' : '02',                    
                    'empty' : False
                }, {
                    'slot_no' : '005',
                    'seat_no' : '03',                    
                    'empty' : True
                }, {
                    'slot_no' : '006',
                    'seat_no' : '01',                    
                    'empty' : False
                }, {
                    'slot_no' : '006',
                    'seat_no' : '02',                    
                    'empty' : False
                }, {
                    'slot_no' : '006',
                    'seat_no' : '03',                    
                    'empty' : True
                }
                ]
            },
            {
                '001003': [{
                    'slot_no' : '004',
                    'seat_no' : '01',
                    'empty' : True
                }, {
                    'slot_no' : '004',
                    'seat_no' : '02',
                    'empty' : True
                }, {
                    'slot_no' : '005',
                    'seat_no' : '01',                    
                    'empty' : True
                }, {
                    'slot_no' : '005',
                    'seat_no' : '01',                    
                    'empty' : True
                }, {
                    'slot_no' : '005',
                    'seat_no' : '02',                    
                    'empty' : True
                }, {
                    'slot_no' : '005',
                    'seat_no' : '03',                    
                    'empty' : True
                }, {
                    'slot_no' : '006',
                    'seat_no' : '01',                    
                    'empty' : False
                }, {
                    'slot_no' : '006',
                    'seat_no' : '02',                    
                    'empty' : False
                }, {
                    'slot_no' : '006',
                    'seat_no' : '03',                    
                    'empty' : False
                }
                ]
            }
        ],
        '하행' : [
            {
                '001004': [{
                    'slot_no' : '004',
                    'seat_no' : '01',
                    'empty' : False
                }, {
                    'slot_no' : '004',
                    'seat_no' : '02',                    
                    'empty' : True
                }, {
                    'slot_no' : '004',
                    'seat_no' : '03',                    
                    'empty' : True
                }, {
                    'slot_no' : '005',
                    'seat_no' : '01',                    
                    'empty' : True
                }, {
                    'slot_no' : '005',
                    'seat_no' : '02',                    
                    'empty' : True
                }, {
                    'slot_no' : '005',
                    'seat_no' : '03',                    
                    'empty' : False
                }, {
                    'slot_no' : '006',
                    'seat_no' : '01',                    
                    'empty' : True
                }, {
                    'slot_no' : '006',
                    'seat_no' : '02',                    
                    'empty' : True
                }, {
                    'slot_no' : '006',
                    'seat_no' : '03',                    
                    'empty' : True
                }
                ]
            },
            {
                '001005': [{
                    'slot_no' : '004',
                    'seat_no' : '01',
                    'empty' : False
                }, {
                    'slot_no' : '004',
                    'seat_no' : '02',
                    'empty' : False
                }, {
                    'slot_no' : '004',
                    'seat_no' : '03',                    
                    'empty' : True
                }, {
                    'slot_no' : '005',
                    'seat_no' : '01',                    
                    'empty' : False
                }, {
                    'slot_no' : '005',
                    'seat_no' : '02',                    
                    'empty' : False
                }, {
                    'slot_no' : '005',
                    'seat_no' : '03',                    
                    'empty' : True
                }, {
                    'slot_no' : '006',
                    'seat_no' : '01',                    
                    'empty' : True
                }, {
                    'slot_no' : '006',
                    'seat_no' : '02',                    
                    'empty' : True
                }, {
                    'slot_no' : '006',
                    'seat_no' : '03',                    
                    'empty' : True
                
                }]
            }
        ],

    }
    return JsonResponse(context)
    

# Create your views here.
def index(request):
    trains = Train.objects.all()
    tt = Train.objects.values('train_no').annotate(total=Count('train_no'))
    print(tt)

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
            return redirect('webserver:detail', train_pk)
        
    else:
        form = TrainForm(instance=train)

    context = {
        'form' : form ,
    }

    return render(request, 'webserver/form.html', context)

def delete(request):
    pass
