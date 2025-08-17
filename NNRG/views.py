from django.shortcuts import render,HttpResponseRedirect,HttpResponse
import smtplib
from . import models
def send_email(receiver, token ,team ):
        if(token == 1):
         try:
          content = "Dear "+team+" Owner" + " Your team is Onboarded in IPL successfully"
          server=smtplib.SMTP('smtp.gmail.com',587)
          server.starttls()
          server.login("YOUR-MAIL-ID",'YOUR-MAIL-PASSWORD')
          server.sendmail('YOUR-MAIL-ID',receiver,content)
         except:
           print("error occured while sending email")
        else:
           pass
def send_email_points(request):
          content = models.points.objects.all().values()
          server=smtplib.SMTP('smtp.gmail.com',587)
          server.starttls()
          server.login('YOUR-MAIL-ID','YOUR-MAIL-PASSWORD')
          server.sendmail('YOUR-MAIL-ID','RECEIVER-MAIL',"this is points table email")
          return HttpResponseRedirect("http://127.0.0.1:8000/IPL/points/")

def go_to_home(request):
   return HttpResponseRedirect('IPL/')

def view_page(request):
   team_list = ['KKR','DC',"RR"]
   cap_list = ['Nithish Rana', 'David warner','Sanju Samson']
   trophes = [2,0,1]
   j = 0
   k = 0
   for i in team_list:
     obj = models.teams()
     obj.name = i
     obj.captain = cap_list[j]
     obj.trophy = trophes[k]
     obj.save()
     j+=1
     k+=1
   return render(request , 'test_home.html')

def view_teams(request):
   list1 = models.teams.objects.all().values()
   return render(request,'view_teams.html',{'teamss':list1})

def view_squad(request):
   list1 = models.players.objects.all().values()
   return render(request,'view_squad.html',{'squad':list1})

def view_points(request):
   list1 = models.points.objects.all().values()
   return render(request,'view_points.html',{'points':list1})

def view_dashboard(request):
   list1 = models.stats.objects.all().values()
   return render(request,'view_dashboard.html',{'stats':list1})
 
def view_stats(request):
   return render(request,'view_stats.html')


 




