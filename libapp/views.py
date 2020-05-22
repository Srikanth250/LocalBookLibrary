from django.shortcuts import render, HttpResponse, redirect
from libapp.models import Book

# Create your views here.
def home(request):
	return render(request, "home.html")

def addbookpage(request):
	return render(request, "addbookpage.html")
	
def addbook(request):
	if request.method == "POST":

		title  = request.POST.get('title', None)
		isbn   = request.POST.get('isbn', None)
		author = request.POST.get('auth', None)
		catg   = request.POST.get('cat', None)
		
		try:
			book_data = Book.objects.get(title=title)
			return HttpResponse(f" Title must be Unique !")
		except Book.DoesNotExist:
			Book.objects.create(title=title, isbn=isbn, author=author, category=catg)
			return HttpResponse(f" Book Added Successfully !")
			
	return render(request, "addbookpage.html")
	
def viewbookpage(request):
	return render(request, "viewbookpage.html")
	
def viewbook(request):
	if request.method == "POST":
		title = request.POST.get('book_title', None)
		
		try:
			book = Book.objects.get(title=title)
			return render(request, "viewbookresults.html", {"books":book})
		except Book.DoesNotExist:
			return HttpResponse(f" No Book Found Matching the Given Title ")
			
	return render(request, "viewbookresults.html")
	
def viewallbookpage(request):
	book = Book.objects.all()
	return render(request, "viewallbookresults.html", {"books":book})
	
def editbook(request, id):
	if request.method == "POST":
		isbn    = request.POST.get('isbn', None)
		author  = request.POST.get('auth', None)
		catg    = request.POST.get('cat', None)
			
		Book.objects.filter(pk=id).update(isbn=isbn, author=author, category=catg)
		return redirect('/viewbookpage/')

	book = Book.objects.get(pk=id)
	return render(request, "editbookpage.html", {"books":book})
	
def deletebook(request, id):
	if id > 0:
		book = Book.objects.get(pk=id)
		book.delete()
		#return HttpResponse(f"Book Deleted !")
		return redirect('/viewbookpage/')
		
	return HttpResponse(f" No matching book found for the passed ID !")