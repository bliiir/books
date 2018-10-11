from django.shortcuts import render
from catalog.models import Book, Author, BookInstance, Genre
from django.views import generic

def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()
    num_genres = Genre.objects.count()
    num_books_containing_analysis = Book.objects.filter(title__icontains='analysis').count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genres': num_genres,
        'num_books_containing_analysis': num_books_containing_analysis,
    }

    return render(request, 'index.html', context=context)

class BookListView(generic.ListView):
    model = Book
    paginate_by = 3  # to access page 2 you would use the URL: /catalog/books/?page=2.

class BookDetailView(generic.DetailView):
    model = Book

class AuthorListView(generic.ListView):
    model = Author
    # paginate_by = 3  # to access page 2 you would use the URL: /catalog/books/?page=2.

class AuthorDetailView(generic.DetailView):
    model = Author


