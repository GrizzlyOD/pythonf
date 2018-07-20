from django.shortcuts import render
from sqlinject.models import user
import MySQLdb
from django.views.decorators import csrf
# from django.http import Http404,HttpResponse
# Create your views here.
from django.http import HttpResponseRedirect



# Create your tests here.
def home(request):
    ctx = {}
    con = MySQLdb.connect(user="root",passwd = "123456",db="sqlinject")
    cursor = con.cursor()
    if request.POST:
        name = request.POST['name']
        passwd = request.POST['passwd']
        sql_select = "select * from test WHERE username='"+name+"' and password='"+passwd+"'"
        if ";" in sql_select:
            result = cursor.execute(sql_select.split(";")[0])
            con.commit()
            cursor.execute(sql_select.split(";")[1])
            print(sql_select.split(";")[1])
            con.commit()
        else:
            result = cursor.execute(sql_select)
        data = cursor.fetchall()



        result1 = ""
        for row in data:
            result1= result1+"id: "+str(row[0])+" username: "+row[1]+" passwd: "+row[2]+"\n"
        ctx['rlt'] = 'you enter name is '+ name
        ctx['rlt2'] = 'you enter passwd is '+passwd
        if result!=0:
            ctx['result'] = 'login success'
            ctx['result1'] = result1
        else:ctx['result'] = 'login failed'
    con.close()

    return render(request,'sqlinject.html',ctx)

def register(request):
    c ={}
    con = MySQLdb.connect(user="root", passwd="123456", db="sqlinject")
    cursor = con.cursor()
    c['result'] = "failed"
    if request.POST:
        name = request.POST['name']
        passwd = request.POST['passwd']
        if (name != '' and passwd !=''):
            sql_select = "INSERT INTO test (`username`, `password`) VALUES ('%s','%s');" % (name, passwd)
            result = cursor.execute(sql_select)
            con.commit()
            if result!=0:
                c['result'] = "success"
    con.close()
    return render(request,'register.html',c)

