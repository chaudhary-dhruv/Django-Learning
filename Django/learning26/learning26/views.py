from django.http import HttpResponse
from django.shortcuts import render

def test(request):
    return HttpResponse("Hello")

def aboutUs(request):
    return render(request , 'aboutus.html')

def contactUs(request):
    return render(request , 'contactus.html')

def homeOld(request):
    return render(request , 'homeOld.html')

def movies(request):
    return render(request , 'movies.html')

def shows(request):
    return render(request , 'shows.html' )

def news(request):
    return render(request , 'news.html')

def reciepe(request):
    ingredients_list = ["Tuar Dal" , "Jeggery" , "Lemon" , "Water"]
    data  = {"name" : "Dal" , 
             "time" : 30 ,
             "ingredients" : ingredients_list
            }
    return render(request , 'reciepe.html' , data)

def team(request):
    players = ["Faf Du Plasis" , "Suresh Raina" , "Dwayne Bravo" ,"MS Dhoni" , "Ravindra Jadeja" , "R Ashwin"]
    data = {"teamName" : "CSK" ,
            "captain" : "MS Dhoni" ,
            "numOfTrophy" : 5,
            "players" : players
            }
    return render(request ,'team.html' , data)