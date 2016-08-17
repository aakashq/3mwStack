from django.db.models import Count, Sum, Avg
from django.shortcuts import render
from .models import *
from django.http import *
# Create your views here.

#this is index view, it just send the data from the db to the html template to show all the sites list
def index(request):
    try:
        pk = sitemodel.objects.all().annotate(a=Count('valuesmodel__a'), b=Count('valuesmodel__b'))
        return render(request,'index.html',{'data':list(pk),'allow':True})
    except Exception as e:
        raise HttpResponseServerError(e)

# this view fucn is called when the data user click on any specific site to see the data
def sitepage(request, id=0):
    try:
        if id == 0:
            raise Http404("Not Found")
        else:
            site = sitemodel.objects.filter(id=id)[:1]
            value = valuesmodel.objects.filter(site=site)
            return render(request, 'site.html', {'data':list(value),'sitename':site[0].name,'allow':True})
    except Exception as e:
        raise HttpResponseServerError(e)

def sumsummary(request):
    try:
        sites=sitemodel.objects.all()
        values=valuesmodel.objects.all()
        kk=list()
        for i in sites:
            a=0.0
            b=0.0
            for k in values:
                if  k.site==i:
                    a=a+float(k.a)
                    b=b+float(k.b)

            kk.append({'name':i.name,'a':a,'b':b,'id':i.id})

        return render (request,'summary.html',{'data':kk,'pagename':'Sum','allow':False,'sum':True})
    except Exception as e:
        raise HttpResponseServerError(e)

def avgsummary(request):
    try:
        kk = list()
        pk = sitemodel.objects.all().annotate(a=Avg('valuesmodel__a'), b=Avg('valuesmodel__b'))

        for i in pk:
            kk.append({'name': i.name, 'a': i.a, 'b': i.b, 'id': i.id})

        return render(request, 'summary.html', {'data': kk, 'pagename': 'Average','allow':False,'sum':False})
    except Exception as e:
        raise HttpResponseServerError(e)
