from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
   "january": "Eat no meat for the entire month!",
   "february": "Walk for at least 20 minutes every day!",
   "march": "Learn Django for at least 20 minutes every day!",
   "april": "Eat no meat for teh entire month!",
   "may": "Walk for at least 20 minutes every day!",
   "june": "Eat no meat for the entire month!",
   "july": "Walk for at least 20 minutes every day!",
   "august": "Learn Django for at least 20 minutes every day!",
   "september": "Eat no meat for the entire month!",
   "october": "Learn Django for at least 20 minutes every day!",
   "november": "Walk for at least 20 minutes every day!",
   "december": "Eat no meat for the entire month!" 
}


# Create your views here.
def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    response_data =f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

    



def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")
        
    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge", args=[redirect_month] )
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported")
