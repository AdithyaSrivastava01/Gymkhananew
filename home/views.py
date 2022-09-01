from django.shortcuts import render,redirect
from home.models import user
from home.models import payment
import mysql.connector as sqltor
x=''
# Create your views here.
def seehome(request):
    if request.session["usr"]==None:
        return redirect("../login")
    print(request.session["usr"])
    return render(request,"home.html",{'usr':request.session["usr"]})
def seesignup(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        age=request.POST['age']
        lst=user()
        lst.name=name
        lst.email=email
        lst.password=password
        lst.age=int(age)
        lst.save()
        request.session['usr']=email
        #global x=email
        return redirect("../home")
       
    else:
        request.session['usr']=None
        return render(request,"signup.html")
        
    
def seelogin(request):

    mycon=sqltor.connect(host="localhost", user="root", passwd="root",database="gymkhana")
    cursor=mycon.cursor()
    s="select*from home_user;"
    cursor.execute(s)
    result=cursor.fetchall()
    

    if request.method =="POST" and 'cancel' not in request.POST :
        email=request.POST['email']
        password=request.POST['password']
    

        for i in result:
            a,c,d,b=i
            if c==email and d==password:
                request.session['usr']=c
                print()
                return redirect("../home")
        else:
            return render(request,"login.html")
    else:
            request.session['usr']=None
            return render(request,"login.html")

def seepayment(request):
    if request.session["usr"]==None:
        return redirect("../login")
    if request.method=="POST":
         c=request.session['usr']
         name=request.POST['ename']
         address=request.POST['address']
         amount=request.POST['amount']
         quantity=request.POST['quantity']
         date=request.POST["dp"]

        # tamount=quantity*amount
         tamount=request.POST["tamount"]
         lst=payment()
         lst.name=name
         lst.tamount=tamount
         lst.quantity=quantity
         lst.address=address
         lst.date=date
         e=user.objects.get(email=c)
         lst.email=e
         print('ee',c)
         lst.save()
        # print(select)
         return render(request,"thankyou.html")
    
    else:
       
        return render(request,"payment.html")
def seethankyou(request):
    if request.session["usr"]==None:
        return redirect("../login")
    return render(request,"thankyou.html")

def seeorders(request):
    if request.session["usr"]==None:
        return redirect("../login")
    c=request.session['usr']
    """mycon=sqltor.connect(host="localhost", user="root", passwd="root",database="gymkhana")
    cursor=mycon.cursor()
    s="select*from home_payment where email_id='{}'".format(c)
    print(s,"op")


    cursor.execute(s)


    p=cursor.fetchall()
    print(pay_list,"lop")
    pay_list=[]
    pay_d={}
    for i in p:
        pay_d[name]=i[1]
        pay_d[tamout]=i[2]
        pay_d[name]=i[1]

    mycon.commit()"""
    pay_list=payment.objects.filter(email_id=c)
    #print(pay_list,"op")
    #print(request.session["usr"],'lcvph')

    return render(request,"orders.html",{"pay_l":pay_list,'usr':request.session["usr"]})
    
def seegym(request):
    if request.session["usr"]==None:
        return redirect("../login")
    return render(request,"gym.html",{'usr':request.session["usr"]})
def seeequipment(request):
    if request.session["usr"]==None:
        return redirect("../login")
    if request.method=="POST":
        print(request.POST)
        #name=request.POST['btn_signup']
        qname=request.POST["eqname"]
        qamt=request.POST["qamount"]
       
        p1=[{'ename':qname,'amount':qamt}]
        print('vgghgh',p1)
        return render(request,"payment.html",{'p':p1})
    else:
         return render(request,"equipment.html",{'usr':request.session["usr"]})
        
   
def seenutrition(request):
    if request.session["usr"]==None:
        return redirect("../login")
    if request.method=="POST":
        print(request.POST)
        #name=request.POST['btn_signup']
        qname=request.POST["eqname"]
        qamt=request.POST["qamount"]
       
        p1=[{'ename':qname,'amount':qamt}]
        print('vgghgh',p1)
        return render(request,"payment.html",{'p':p1})
    else:
        return render(request,"nutrition.html",{'usr':request.session["usr"]})
        
def seeaccessories(request):
    if request.session["usr"]==None:
        return redirect("../login")
    if request.method=="POST":
        print(request.POST)
        #name=request.POST['btn_signup']
        qname=request.POST["eqname"]
        qamt=request.POST["qamount"]
       
        p1=[{'ename':qname,'amount':qamt}]
        print('vgghgh',p1)
        return render(request,"payment.html",{'p':p1})
    else:
         return render(request,"accessories.html",{'usr':request.session["usr"]})
        


