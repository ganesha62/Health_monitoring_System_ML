from django.shortcuts import render
from joblib import load
model= load('./savedModels/model3.joblib')
# Create your views here.
def mainlung(request):
    return render(request, 'mainlung.html')

def formInfo3(request):
    cob= request.GET['cob']
    au = request.GET['au']
    ps = request.GET['ps']
    ob= request.GET['ob']
    smo= request.GET['smo']
    bd= request.GET['bd']
    cp= request.GET['cp']
    ft= request.GET['ft']
    ap=request.GET['ap']
    gr=request.GET['gr']
    y_pred= model.predict([[cob,au,ps,ob,smo,bd,cp,ft,ap,gr]])
    print(y_pred)
    if y_pred[0]==0:
        #y_pred= 'Not Chronic'
        return render(request, 'lowresult3.html')
    elif y_pred[0]==1:
        return render(request, 'mediumresult3.html')
    else:
        return render(request, 'highresult3.html')
