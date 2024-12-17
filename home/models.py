from django.db import models

# create your models here.

class Departments(models.Model):
    dep_name = models.CharField(max_length=200,null=True,blank=True)
    dep_captions = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.dep_name




class Doctors(models.Model):
    doc_name = models.CharField(max_length=255,null=True,blank=True)
    doc_spec = models.CharField(max_length=255,null=True,blank=True)
    dep_name = models.ForeignKey(Departments, on_delete=models.CASCADE,null=True,blank=True)
    doc_image = models.ImageField(upload_to='doctors',null=True,blank=True)
    
    def __str__(self):
        return 'Dr ' +  self.doc_name + ' -(' + self.doc_spec + ')'

class Booking(models.Model):
    p_name = models.CharField(max_length=255,null=True,blank=True)
    p_phone = models.CharField(max_length=10,null=True,blank=True)
    p_email = models.EmailField(null=True,blank=True)
    doc_name = models.ForeignKey(Doctors, on_delete=models.CASCADE,null=True,blank=True)
    booking_date = models.DateField(null=True,blank=True)
    booked_on = models.DateField(auto_now=True)

    

