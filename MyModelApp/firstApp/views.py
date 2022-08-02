
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Employees
from .models import student
# =========================================================================================================
#                       Here start from Employees
# =========================================================================================================
# Create your views here.
# ==========================Here start main page================================
def main(req):
    return render(req,'main.html')
# =======================here start home page=========================
def home(req):
    return render(req,'home.html')

# =====================here start the insert the data=====================
def insert(req):
    return render(req,'insert.html')

def insertTask(req):
    fname=req.POST.get("Firstname")
    lname=req.POST.get("Lastname")
    salary=req.POST.get("salary")
    deg=req.POST.get("deg")
    email=req.POST.get("email")
    Passw=req.POST.get("passw")
    mob=req.POST.get("mob")
    Add=req.POST.get("Address")
    ob=Employees()
    ob.Firstname=fname
    ob.Lastname=lname
    ob.salary=salary
    ob.deg=deg
    ob.email=email
    ob.passw=Passw
    ob.mob=mob
    ob.Address=Add
    ob.save()
    return render(req,'home.html')

# ========================here start the show the data=====================================
def show(req):
    # select * from Eployees==objects.all()
    rec=Employees.objects.all()

    # select * from Eployees where id=1
    # rec=Employees.objects.filter(id=1)

    # select * from Employess where salary=12500 and name="anoop"
    # rec=Employees.objects.filter(email="shu@gmail.com",Address="vidisha")

    #select * from Employee where salary>50000
    # rec=Employees.objects.filter(salary__gt=50000)

    # for less than
    # rec=Employees.objects.filter(salary__lt=50000)

    # for greater than are equal to <=
    # rec=Employees.objects.filter(salary__gte=50000)

    # for less than are equal to >=
    # rec=Employees.objects.filter(salary__lte=50000)

    # strart with
    # rec=Employees.objects.filter(Firstname__startswith="k")

    # in every where
    # rec=Employees.objects.filter(Firstname__icontaints="oo",Lastname__icontaints="oo")
    return render(req,'show.html',{'rec':rec})

# ====================================here start the show indivisual data==================
def details(req):
    return render(req,'details.html')
    
def showTask(req):
    email=req.POST.get("email")
    passw=req.POST.get("passw")
    ob=Employees()
    ob.email=email
    ob.passw=passw
    rec=Employees.objects.filter(email=email,passw=passw)
    return render(req,'details.html',{'rec':rec})


# ==============================Here start the update the data===========================================
def update(req):
    return render(req,'update.html')

def updateTask(req):
    Id=req.POST["Id"]
    fname=req.POST["Firstname"]
    lname=req.POST["Lastname"]
    salary=req.POST["salary"]
    deg=req.POST["deg"]
    email=req.POST["email"]
    Passw=req.POST["passw"]
    mob=req.POST["mob"]
    Add=req.POST["Address"]
    ob=Employees.objects.get(id=Id)
    
    ob.Firstname=fname
    ob.Lastname=lname
    ob.salary=salary
    ob.deg=deg
    ob.email=email
    ob.passw=Passw
    ob.mob=mob
    ob.Address=Add
    ob.save()
    return render(req,'home.html')

# ===========================here start the delet the data==============================
def delete(req):
    return render(req,'delete.html')

def deleteTask(req):
    Id=req.POST["Id"]
    ob=Employees.objects.get(id=Id).delete()
    # ob.id=id
    return render(req,'delete.html')


# =========================================================================================================
#                       Here End from Employees
# =========================================================================================================

# ********************************************************************************************************

# =========================================================================================================
#                       Here start from student
# =========================================================================================================

# =============================here start from student home page===========================================
def stuhome(req):
    return render(req,'stuhome.html')

# =============================here start from student insert page===========================================
def stuInsert(req):
    return render(req,'stuinsert.html')

def stuInsertTask(req):
    fname=req.POST.get("firstname")
    lname=req.POST.get("lastname")
    fathern=req.POST.get("Fathername")
    std=req.POST.get("std")
    rollno=req.POST.get("rollno")
    phymarks=req.POST.get("PhyMarks")
    chemarks=req.POST.get("CheMarks")
    mathmarks=req.POST.get("MathMarks")
    email=req.POST.get("email")
    Passw=req.POST.get("password")
    mob=req.POST.get("mob")
    Add=req.POST.get("Add")
    ob=student()
    ob.firstname=fname
    ob.lastname=lname
    ob.Fathername=fathern
    ob.std=std
    ob.rollno=rollno
    ob.PhyMarks=phymarks
    ob.CheMarks=chemarks
    ob.MathMarks=mathmarks
    ob.email=email
    ob.password=Passw
    ob.mob=mob
    ob.Add=Add
    ob.save()
    return render(req,'stuhome.html')

# =============================here start from student show page===========================================
def studetails(req):
    data=student.objects.all()
    return render(req,'studetails.html',{'data':data})

# =============================here start from student update page===========================================
def stuupdate(req):
    return render(req,'stuupdate.html')


def stuupdateTask(req):
    Id=req.POST["Id"]
    fname=req.POST["firstname"]
    lname=req.POST["lastname"]
    Fname=req.POST["Fathername"]
    std=req.POST["std"]
    rollno=req.POST["rollno"]
    pmarks=req.POST["PhyMarks"]
    cmarks=req.POST["CheMarks"]
    Mmarks=req.POST["MathMarks"]
    email=req.POST["email"]
    Passw=req.POST["password"]
    mob=req.POST["mob"]
    Add=req.POST["Add"]
    ob=student.objects.get(id=Id)
    
    ob.firstname=fname
    ob.lastname=lname
    ob.Fathername=Fname
    ob.std=std
    ob.rollno=rollno
    ob.PhyMarks=pmarks
    ob.CheMarks=cmarks
    ob.MathMarks=Mmarks
    ob.email=email
    ob.password=Passw
    ob.mob=mob
    ob.Add=Add
    ob.save()
    return render(req,'stuhome.html')
# =============================here start from student delete page========================================
def studelete(req):
    return render(req,'studelete.html')

def studeleteTask(req):
    Id=req.POST["Id"]
    ob=student.objects.get(id=Id).delete()
    # ob.id=id
    return render(req,'stuhome.html')
# =============================here start from student home page===========================================
