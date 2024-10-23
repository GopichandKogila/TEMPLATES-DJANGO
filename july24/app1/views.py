from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,"about.html")
    

def help(request):
    return render(request,'help.html')

def signUp(request):
    return render(request,'empty.html')

def func(request,num):
    result = (num%2==0)
    d={'result':result}
    return render(request,'evenodd.html',d)

def func2(request,sname):
    res=(sname==sname[::-1])
    d={'result':res} 
    return render(request,'palin.html',d)