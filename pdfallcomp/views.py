from django.shortcuts import render,HttpResponse
from pdfallcomp.models import Pdfallcomp
# Create your views here.
def pdfallcomp (request):
    pdf= Pdfallcomp.objects.all()
    context= {'pdf': pdf}
    return render (request,'pdf/pdfallcomp.html',context)