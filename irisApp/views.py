from django.shortcuts import render
from joblib import load
model= load('./savedModels/model.joblib')
# Create your views here.
def predictor(request):
    return render(request, 'main.html')

def formInfo(request):
    wc= request.GET['wc']
    bgr = request.GET['bgr']
    bu = request.GET['bu']
    sc= request.GET['sc']
    pcv= request.GET['pcv']
    al= request.GET['al']
    hemo= request.GET['hemo']
    age= request.GET['age']
    #su=request.GET['su']
    #htn=request.GET['htn']
    y_pred= model.predict([[wc,bgr,bu,sc,pcv,al,hemo,age]])
    print(y_pred)
    if y_pred[0]==0:
        #y_pred= 'Not Chronic'
        return render(request, 'notchroresult.html')
    else:
        return render(request, 'chroresult.html')
        #y_pred= 'Chronic'
    #return render(request, 'result.html', {'result': y_pred})