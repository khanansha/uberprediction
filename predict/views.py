from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import pandas as pd
import numpy as np
# Create your views here.

# from sklearn.externals import joblib
import joblib
import pickle
import request

reloadModel = pickle.load(open('./models/taxi.pkl', 'rb'))
print(reloadModel)


def index(request):
    return render(request, 'index.html')


def predict(request):

    if request.method == 'POST':
        # temp = {}
        # temp['Priceperweek'] = request.POST.get('Priceperweek')
        # temp['Population'] = request.POST.get('Population')
        # temp['Monthlyincome'] = request.POST.get('Monthlyincome')
        # temp['weight'] = request.POST.get('weightVal')

        # testDtaa = pd.DataFrame({'x': temp}).transpose()
        # scoreval = reloadModel.predict(testDtaa)[0]
        Priceperweek = request.POST.get('Priceperweek', '')
        Population = request.POST.get('Population', '')
        Monthlyincome = request.POST.get('Monthlyincome', '')
        Averageparkingpermonth = request.POST.get('Averageparkingpermonth', '')
        # int_features = [int(x) for x in request.POST.get(
        #     'Priceperweek', 'password', 'Monthlyincome', 'Averageparkingpermonth')]
        print(Averageparkingpermonth)
        pri = int(Priceperweek)
        pop = int(Population)
        mon = int(Monthlyincome)
        Ave = int(Monthlyincome)

        features = [[pri, pop, mon, Ave]]
        print(features)
        # int_features = [for x in request.POST.values()]
        final_features = [np.array(features)]
        prediction = reloadModel.predict(features)
        context = {'prediction': prediction}

        return render(request, 'index.html', context)
    else:
        return HttpResponse("sorry")


def ran(request):
    if request.method == 'POST':

        Priceperweek = request.POST.get('Priceperweek', '')
        Population = request.POST.get('Population', '')
        Monthlyincome = request.POST.get('Monthlyincome', '')
        Averageparkingpermonth = request.POST.get('Averageparkingpermonth', '')
        print(Averageparkingpermonth)
        pri = int(Priceperweek)
        pop = int(Population)
        mon = int(Monthlyincome)
        Ave = int(Averageparkingpermonth)

        features = [[pri, pop, mon, Ave]]
        print(features)
        # int_features = [for x in request.POST.values()]
        # final_features = [np.array(features)]
        prediction = reloadModel.predict(features)
        print(prediction)
        context = {'prediction': prediction}

        return HttpResponse(prediction)
    else:
        return HttpResponse("sorry")


def check(request):

    Priceperweek = request.GET.get('Priceperweek')
    Population = request.GET.get('Population')
    Monthlyincome = request.GET.get('Monthlyincome')
    Averageparkingpermonth = request.GET.get('Averageparkingpermonth')
    pri = int(Priceperweek)
    pop = int(Population)
    mon = int(Monthlyincome)
    Ave = int(Averageparkingpermonth)
    features = [[pri, pop, mon, Ave]]
    print(features)
    # int_features = [for x in request.POST.values()]
    final_features = [np.array(features)]
    prediction = reloadModel.predict(features)

    return HttpResponse(prediction)
