from django.contrib import admin

from books.models import Book, Borrow, User

admin.site.register([User,Book,Borrow])