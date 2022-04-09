from django.shortcuts import render
from .models import Book_Information
from .forms import Add_Book
# Create your views here.

def add_book(request):
    context = {}
    form = Add_Book(request.POST or None)

    if form.is_valid():
       # b_id = form.cleaned_data["book_id"]
        b_title = form.cleaned_data["book_title"]
        b_author = form.cleaned_data["book_author"]
        b_cost = form.cleaned_data["book_cost"]
        b_quantity = form.cleaned_data["book_quantity"]

        #book_details = Book_Information(book_id = b_id, book_title = b_title, book_author = b_author, book_cost = b_cost, book_quantity = b_quantity)\
        if(form.save() == True):
            pass
        else:
            print("value not saved")

    context['form'] = form

    return render(request, "add_book.html", context)

def get_book_data(request):

    context = {}

    form = Add_Book(request.GET or None)

    if request.method == "GET":

        book_id = request.GET.get('book_id')

        context['book_details'] = Book_Information.objects.all().filter( id = book_id)

        return render(request , "view_book_by_id.html", context)

def view_all_book(request):
    context = {}

    context["data"] = Book_Information.objects.all()

    return render(request, "view_all_book.html", context)

