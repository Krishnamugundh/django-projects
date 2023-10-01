from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpRequest
from .forms import pat_form,new_data
from .models import pat_desc,user_input

# Create your views here.

def login_doc(request):
    pat = pat_desc.objects.all().values()
    context = {'names':pat}
    return render(request,'login.html',context)

def hello(request):
    print('hello hi this is mugundh')
    return HttpResponse("Helo world")

# def createPat(request):
#     # form = pat_form(request.POST)
#     # print(request.POST)
#     # if request.method=='POST':
#     #     print(request.POST)
#     #     form = pat_form(request.POST)
#     #     if form.is_valid():
#     #         form.save()
#     #         redirect('login/')
#     if request.POST:
#         form = pat_form(request.POST)
#         print(request.POST)
#         if form.is_valid():
#             form.save()
#         return redirect('login')
    
#     # context = {'form' : form}
#     return render(request,'pat_desc.html',{'form' : pat_form})

def createPat(request):
    # print('hello hi this is krishna')
    
    # if request.method == "post":
    #     print('hello hi this is mugundh')
    #     form = pat_form(request.POST)
    #     print('hello hi this is mugundh1')
    #     if form.is_valid():
    #         instance = form.save(commit=False)
    #         text = form.cleaned_data()
    #         instance.save()
    #         print('hello hi this is mugundh2')
    #         return redirect('login')
    # else:
    #     form = pat_form()
    #     print('hello hi this is mugundh3')
            
    # print(form.errors)
    form = pat_form()
    if request.method == 'POST':
        print(request.POST)
    return render(request, 'pat_desc.html', {'form': form})

def createNew(request):
    form1 = new_data()
    if(request.method == 'POST'):
        print(request.POST)
    context = {'form':form1}
    return render(request,'new_desc.html', context)