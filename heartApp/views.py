from django.shortcuts import render
from joblib import load
model= load('./savedModels/model2.joblib')
# Create your views here.
def mainheart(request):
    return render(request, 'mainheart.html')
def formInfo2(request):
    thalach= request.GET['thalach']
    oldpeak = request.GET['oldpeak']
    cp = request.GET['cp']
    ca= request.GET['ca']
    exang= request.GET['exang']
    chol= request.GET['chol']
    age= request.GET['age']
    trestbps= request.GET['trestbps']
    slope=request.GET['slope']
    sex=request.GET['sex']
    y_pred= model.predict([[thalach,oldpeak,cp,ca,exang,chol,age,trestbps,slope,sex]])
    print(y_pred)
    if y_pred[0]==0:
        #y_pred= 'Not Chronic'
        return render(request, 'notchroresult2.html')
    else:
        return render(request, 'chroresult2.html')
