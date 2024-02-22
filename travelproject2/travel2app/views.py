from django.http import HttpResponse
from django.shortcuts import render
from . models import rooms
from . models import testimonial
# Create your views here.
def demo(request):
   obj=rooms.objects.all()
   obj1=testimonial.objects.all()

   return render(request,"index.html",{'rooms_data':obj,'testimonial_data':obj1})



# def arithmetic_operations(request):
#    x=int(request.GET['num1'])
#    y=int(request.GET['num2'])
#    addition=x+y
#    subtraction=x-y
#    multiplication=x*y
#    division=x/y
#    return render(request,"result.html",{'addition':addition,'subtraction':subtraction,'multiplication':multiplication,'division':division})
