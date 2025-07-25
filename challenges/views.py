from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
# Create your views here.
def index(request):
    list_items=""
    months=list(monthly_challenges.keys())
    return render(request,"challenges/index.html",{
        "months":months
    })

monthly_challenges={
    "january":"Eat no meat for the entire month",
    'february':"Walk for 20 mins everyday!",
    'march':"Learn Django for at least 20 mins every day!",
    'april':"Eat no meat for the entire month",
    'may':"Walk for 20 mins everyday!",
    'june':"Learn Django for at least 20 minns every day!",
    'july':"Eat no meat for the entire month",
    'august':"Walk for 20 mins everyday!",
    'september':"Learn Django for at least 20 minns every day!",
    'october':"Eat no meat for the entire month",
    'november':"Walk for 20 mins everyday!",
    'december':"Learn Django for at least 20 minns every day!"
    
    
    
}

def monthly_challenge_by_number(request,month):
    months=list(monthly_challenges.keys())

    if month >len(months):
        return HttpResponseNotFound("Invalid month")
    

    redirect_month=months[month-1]
    redirect_path=reverse('month-challenge',args=[redirect_month])
    return HttpResponseRedirect(redirect_path)






def monthly_challenge(request,month):
    try:
       challenge_text=monthly_challenges[month]
       return render(request,"challenges/challenge.html",{
           "text":challenge_text,
           "month_name":month

       })
       
    except:
       return HttpResponseNotFound("<h1>This month is not supported!</h1>")
    
        
