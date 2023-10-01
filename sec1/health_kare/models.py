from django.db import models

# Create your models here.

class pat_desc(models.Model):
    pat_id = models.IntegerField()
    pat_name = models.CharField(max_length=35)
    desc = models.TextField(max_length=100,blank=True,default='Please enter some text')
    age = models.PositiveIntegerField()
    updated = models.DateField(auto_now=True)
    created = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f'Patient name : {self.pat_id} //  Age : {self.age}'
    
    class Meta:
        ordering = ['updated','pat_id']

class doc_desc(models.Model):
    doc_id = models.IntegerField()
    doc_name = models.CharField(max_length=25)
    patient_id = models.ForeignKey(pat_desc,on_delete=models.CASCADE)
    age = models.PositiveIntegerField()
    updated = models.DateField(auto_now=True)
    created = models.DateField(auto_now_add=True)
    
    
class user_input(models.Model):
    name = models.CharField(max_length=500,null=True,blank=True)
    age = models.SmallIntegerField(null=True,blank=True)
    place = models.TextField(null=True,blank=True)