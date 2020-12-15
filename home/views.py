from django.shortcuts import render,HttpResponse
from.models import Contact
from django.contrib import messages
from pdfdownload.models import pdftute 
#pdftute is pdfmath
from pdfenglish.models import Pdfenglish
from pdfallcomp.models import Pdfallcomp
from itertools import islice, chain

# Create your views here.
def home(request):
    return render(request,'home/home.html')
    #return HttpResponse('this is home')
def contact(request):
    if request.method =='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<2 :
            contact= Contact.objects.none
            messages.error(request,'Please fill the form correctly !')
        else:
            contact=Contact(name=name,email=email,phone=phone,content=content)
            contact.save()
            messages.success(request,'Your message is sent !')
    return render(request,'home/contact.html')
def about(request):
    return render(request,'home/about.html')
def search(request):
    query= request.GET['query']
    if len(query) > 50 or len(query) == 0:  
        pdfmath= pdftute.objects.none()
        pdfenglish=Pdfenglish.objects.none()
        pdfallcomp=Pdfallcomp.objects.none()
        pdf=sorted(chain(pdfenglish,pdfmath,pdfallcomp))
    else:
        pdfmath=pdftute.objects.filter(title__icontains=query) 
        pdfenglish=Pdfenglish.objects.filter(title__icontains=query)
        pdfallcomp=Pdfallcomp.objects.filter(title__icontains=query)
        pdf=sorted(chain(pdfenglish,pdfmath,pdfallcomp,))
    #if pdf.count() == 0:
        #messages.error(request,'Please fill the form correctly !')
    params={'pdf':pdf , 'query':query}
    return render(request,'home/search.html',params)
    
    #return HttpResponse('this is search')    