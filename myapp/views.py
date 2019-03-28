from django.shortcuts import render
from django.contrib.auth import login, authenticate,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from .models import UserProfile,Agromain,Agridata,Contact
from django.core.urlresolvers import reverse
import pandas as pd
from django.db.models import Avg
from graphos.sources.simple import SimpleDataSource
from graphos.renderers.highcharts import LineChart,BarChart,ScatterChart,ColumnChart
from mysite.settings import BASE_DIR
from sklearn.cluster import MeanShift,estimate_bandwidth
from sklearn import linear_model
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt






def log_in(request):
    if request.method == 'POST':
        phone=request.POST.get('phone')
        password=request.POST.get('password')
        user=authenticate(username=phone,password=password)
        print user,phone,password
        if user :
            userpro=UserProfile.objects.get(username=user)
            
            if userpro :
                login(request,user)
                return HttpResponseRedirect(reverse('home_url'))
            else:
                return render(request,'login.html',{'error':"sorry,unable to login"})

        else:
            return render(request,'login.html',{'error':"sorry,unable to login"})
    else:
        return render(request,'login.html',{})      


def signup(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        password=request.POST.get('pass1')
        user=User.objects.create_user(
            username=phone,
            email=email,
            password=password,
            )
            
        userpro=UserProfile(
            username=user,
            email=email,
            phone=phone)

        userpro.save()
        return render(request,'login.html',{})
    else:
        return render(request,'signup.html',{})    

def home(request):
    return render(request,'home.html',{})
def log_out(request):
    logout(request)
    return render(request,'home.html',{})   
def create_js_chart(name='ERNAKULAM',html_id='highchart_div',title = 'ERNAKULAM'):
    district = Agridata.objects.filter(district_name__icontains=name)
    years = [int(value[0]) for value in district.values_list('crop_year').distinct()]
    averages = [
        (Agridata.objects.filter(district_name=name, crop_year=year).aggregate(
            Avg('production'))).get('production__avg') for year in years
    ]
    data = [
        ['Years', 'Production (Avg)'],
    ]
    for year, avg in zip(years, averages):
        data.append([year, avg])
    
    sd = SimpleDataSource(data)
    hc = LineChart(
        sd, html_id, height=450, width=450,
        options={'title': title, 'xAxis': {'title': {'text':'years'}}, 'style': 'float:right;'}
    )
    return hc
def home(request):
    if request.method == 'POST':
        if "file1" in request.FILES:
            print(request.user)
            if request.user.is_authenticated:
                file1 = request.FILES['file1']
                print(file1)
                analysis = Agromain(data_file=file1)
                print (analysis)
                analysis.save()
                ernakulam = create_js_chart()
                alappuzha = create_js_chart('ALAPPUZHA','highchartala_div','ALAPPUZHA')
                idukki = create_js_chart('IDUKKI','highchartidukki_div','IDUKKI')
                kannur = create_js_chart('KANNUR','highchartkannur_div','KANNUR')
                kasaragod = create_js_chart('KASARAGOD','highchartkasaragod_div','KASARAGOD')
                kollam = create_js_chart('KOLLAM','highchartkollam_div','KOLLAM')
                kottayam = create_js_chart('KOTTAYAM','highchartkottayam_div','KOTTAYAM')
                kozhikode = create_js_chart('KOZHIKODE','highchartkozhikode_div','KOZHIKODE')
                malappuram = create_js_chart('MALAPPURAM','highchartmala_div','MALAPPURAM')
                palakad = create_js_chart('PALAKKAD','highchartpala_div','PALAKKAD')
                pathanamthitta = create_js_chart('PATHANAMTHITTA','highchartpathanam_div','PATHANAMTHITTA')
                tvm = create_js_chart('THIRUVANANTHAPURAM','highcharttvn_div','THIRUVANANTHAPURAM')
                tsr = create_js_chart('THRISSUR','highcharttsr_div','THRISSUR')
                wayanad = create_js_chart('WAYANAD','highchartwayanad_div','WAYANAD')
                # data = pd.read_csv(file1)
                # Agridata.objects.all().delete()
                # state =[i for i in data['state_name']]
                # district_name = [i for i in data['district_name']]
                # crop_year = [i for i in data['crop_year']]
                # season = [i for i in data['season']]
                # crop = [i for i in data['crop']]
                # area = [i for i in data['area']]
                # production = [i for i in data['production']]
                # rainfall = [i for i in data['rainfall']]
                # for i in range(len(state)):
                #   agri = Agridata(state_name=state[i],district_name=district_name[i],crop_year=crop_year[i],
                #       season=season[i],crop=crop[i],area=area[i],production=production[i],rainfall=rainfall[i])
                #   agri.save()
                msg = "ok"

                return render(request, 'home.html', {'msg':msg,'wayanad':wayanad,'tsr':tsr,
                    'tvm':tvm,'pathanamthitta':pathanamthitta,'palakad':palakad,
                    'malappuram':malappuram,'kozhikode':kozhikode,'kottayam':kottayam,
                    'kollam':kollam,'kasaragod':kasaragod,
                    'kannur':kannur,'idukki':idukki, 'alappuzha':alappuzha,'ernakulam':ernakulam})
            else:

                file1 = None
                return render(request, 'home.html', {})
        else:

            file1 = None
            return render(request, 'home.html', {})
        
    else:
        ernakulam = create_js_chart()
        return render(request, 'home.html', {})


def About(request):
    ernakulam = create_chart()

    return render(request, 'about.html', {})


def cluster(request):
    data = Agromain.objects.filter(active=True)[0]
    filename = "{}/media/{}".format(BASE_DIR,data.data_file)
    df = pd.read_csv(filename)
    print(type(df))
    print(df['rainfall'])
    rf = df['rainfall']
    gf = df['district_name'].unique()
    dist = gf.tolist()
    x=[]

    for i in rf:
        x.append(i)

    y = tuple(x)

    # x = df['rainfall']
    X = np.array(zip(x,range(len(x))), dtype=np.int)
    # print(X)
    
    bandwidth = estimate_bandwidth(X, quantile=0.1)
    print ("bandwidth",bandwidth)
    ms = MeanShift(bandwidth=bandwidth, bin_seeding=True)
    print (ms)
    ms.fit(X)
    labels = ms.labels_
    print("labels",labels)
    cluster_centers = ms.cluster_centers_
    n_clusters_ = len(dist)
    for k in range(n_clusters_):
        my_members = labels == k
        print "cluster {0}: {1}".format(k, X[my_members,0])
    colors = 10*['r.','g.','b.','c.','k.','y.','m.']
    r,g,b,c,k,y,m=[],[],[],[],[],[],[]
    for i in range(len(X)):
        if colors[labels[i]] == 'r.':
            r.append([X[i][0],X[i][1]])
        elif colors[labels[i]] == 'g.':
            g.append([X[i][0],X[i][1]])
        elif colors[labels[i]] == 'b.':
            b.append([X[i][0],X[i][1]])
        elif colors[labels[i]] == 'c.':
            c.append([X[i][0],X[i][1]])
        elif colors[labels[i]] == 'k.':
            k.append([X[i][0],X[i][1]])
        elif colors[labels[i]] == 'y.':
            y.append([X[i][0],X[i][1]])
        else:
            m.append([X[i][0],X[i][1]])

        plt.plot(X[i][0], X[i][1], colors[labels[i]], markersize = 10)

    

    print("ggggggggggggggggg",g)


    vals = X.tolist()

    return render(request,'cluster.html',{'vals':vals,'r':r,'g':g,'b':b,'c':c,'k':k,'y':y,'m':m})  

def About(request):
    return render(request,'about.html',{})
def contact(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        s=Contact(name=name,email=email,message=message)
        s.save()
        return render(request,'contact.html',{'message':"hloo"})

    else:
        return render(request,'contact.html',{})    




def prediction(request):
    if request.method == 'POST':
        Area=request.POST.get('area')
        Crop=request.POST.get('crop')
        Rainfall=request.POST.get('rainfall')
        # production=request.POST.get('production')
        return render(request,'predict.html',{})
    else:
        return render(request,'home.html',{})

    