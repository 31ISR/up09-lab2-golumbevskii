from django.shortcuts import render

def about(req):
    return render(req, "about.html")
def Home(req):
    return render(req, "Home.html")