from django.shortcuts import render

def index(request):
    return render(request , 'index.html')



def addlisting (request):
    return render(request , 'add-listing.html')


def boukings (request) :
    return render (request , 'bookings.html')

def bookmarks (request) :
    return render (request , 'bookmarks.html')

def charts(request):
    return render  (request , 'charts.html')

def docktorprof(request):
        return render  (request , 'doctor-profile.html')

def messages (request):
     return render (request , "messages.html")

def reviews(request):
     return render (request , 'reviews.html')

def tables(request):
     return render (request , 'tables.html')
def user(request) : 
     return  render (request , 'user-profile.html')