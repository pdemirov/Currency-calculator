from django.shortcuts import render
from . models import Currencies
from . forms import CalcForm, AddForm


def allcurrencies(request):
    all_curr = Currencies.objects.all()
    context = {
        'all_curr': all_curr
    }
    return render(request, 'calc/allcurrencies.html', context)


def calculate(request):
    if request.method == 'POST':
        form = CalcForm(request.POST)
        if form.is_valid():

            qtity = form.cleaned_data['qtity']
            from_curr = form.cleaned_data['from_curr']
            to_curr = form.cleaned_data['to_curr']

            print(qtity, from_curr, to_curr)

    form = CalcForm()

    return render(request, 'calc/calculate.html', {'form': form})


def add_curr(request):

    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            form.save()

    form = AddForm()

    return render(request, 'calc/addcurrencies.html', {'form': form})
