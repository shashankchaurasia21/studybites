from django.shortcuts import render,HttpResponse
from pdfdownload.models import pdftute

# Create your views here.
def pdfhome(request):
    return render(request,'pdf/pdfhome.html')
def pdfmath(request):
    pdf= pdftute.objects.all()
    context={'pdf':pdf}
    return render(request,'pdf/pdfmath.html',context)
