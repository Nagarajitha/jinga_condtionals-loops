from django.shortcuts import render

# Create your views here.

def condtion_if(request):
    d={'a':5,'b':7}
    return render(request,'condtion_if.html',context=d)

def condition_elif(request):
    d={'a':4,'b':5,'c':9}
    return render(request,'condition_elif.html',d)

def for_loop(request):
    d={'name' :'RANJITHA'}
    return render(request,'for_loop.html',context=d)