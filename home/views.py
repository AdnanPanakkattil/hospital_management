from django.shortcuts import render
from django.http import HttpResponse
from. forms import BookingForm

from .models import Departments, Doctors

 # Create your views here.
def index(reguest):

    return render(reguest, 'index.html')

def about(reguest):
    
   return render(reguest, 'About.html')

def booking(reguest):
   if reguest.method =="POST":
      form = BookingForm(reguest.POST)
      if form.is_valid():
          form.save()
          
   form = BookingForm()
   dict_form = {
      'form': form
   }
   return render(reguest, 'booking.html', dict_form)

def doctors(reguest):
   dict_docs = {
      'doctors':Doctors.objects.all()
   }
   return render(reguest, 'doctors.html', dict_docs )

def contact(reguest):
   return render(reguest, 'contact.html')

def department(reguest):
   dict_dept={
      'dept':Departments.objects.all()
   }
   return render(reguest, 'department.html',dict_dept)


#ttttt