from django.shortcuts import render
from django.views import generic

# Create your views here.
from .models import Book, Author, BookInstance, Genre

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()
    num_genres = Genre.objects.count()
    
    num_visits = request.session.get('num_visits', 0)
    num_visits += 1
    request.session['num_visits'] = num_visits

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genres': num_genres,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

class BookListView(generic.ListView):
    model = Book
    paginate_by = 10
    context_object_name = 'book_list'   # your own name for the list as a template variable
    queryset = Book.objects.all() # Get 5 books containing the title war
    template_name = 'books/my_arbitrary_template_name_list.html'  # Specify your own template name/location

class BookDetailView(generic.DetailView):
    model = Book

class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 10
    context_object_name = 'author_list'   # your own name for the list as a template variable
    queryset = Author.objects.all() # Get 5 books containing the title war
    template_name = 'authors/my_arbitrary_template_name_list.html'  # Specify your own template name/location

class AuthorDetailView(generic.DetailView):
    model = Author
