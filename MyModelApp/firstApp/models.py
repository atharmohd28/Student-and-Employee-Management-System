
import email
from django.db import models

# Create your models here.
# ==========================================Here start the Employees Table=================================
class Employees(models.Model):
    Firstname=models.CharField(max_length=20)
    Lastname=models.CharField(max_length=20)
    salary=models.FloatField()
    deg=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    passw=models.CharField(max_length=20)
    mob=models.IntegerField()
    Address=models.CharField(max_length=50)
    
    
    
    def __str__(self):
        s=self.Firstname + self.Lastname + str(self.salary) + self.deg+ self.email+ self.passw+str(self.mob)+self.Address
        return s




# =========================================================================================================
#  =====================Here start the Student Table==================================================
# ====================================================================================================
class student(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    Fathername=models.CharField(max_length=20)
    std=models.CharField(max_length=20)
    rollno=models.IntegerField()
    PhyMarks=models.IntegerField()
    CheMarks=models.IntegerField()
    MathMarks=models.IntegerField()
    email=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    mob=models.IntegerField()
    Add=models.CharField(max_length=50)

    def __str__(self):
        r=self.firstname+self.lastname+self.Fathername+self.std+str(self.rollno)
        +str(self.PhyMarks)+str(self.CheMarks)+str(self.MathMarks)+self.email+self.password
        +str(self.mob)+self.Add
        return r