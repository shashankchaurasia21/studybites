from django.shortcuts import render,HttpResponse
from pdfenglish.models import Pdfenglish
# Create your views here.
def pdfenglish(request):
    pdf= Pdfenglish.objects.all()
    context= {'pdf': pdf}
    return render (request,'pdf/pdfenglish.html',context)
    