from django.shortcuts import render

# Create your views here.




def Homepage_view(request):

    return render(request, "Homepage.html")