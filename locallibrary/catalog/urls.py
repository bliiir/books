from django.urls import path
from catalog import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
    # path(r'^book.*\?from=\d{4}.\d{2}.\d{2}.*&to=\d{4}.\d{2}.\d{2}', views.BookDateRangeView.as_view(), name='book_dates')
]




