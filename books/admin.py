from django.contrib import admin
from django.utils import timezone

from .models import Publisher, Author, Book


def display_book_authors(obj):
    return ", ".join([author.first_name for author in obj.authors.all()])

display_book_authors.short_description = 'Authors'


def make_book_pub_date_to_now(modeladmin, request, queryset):
    queryset.update(publication_date=timezone.now())

make_book_pub_date_to_now.short_description = 'Mark selected book pub_date as now'

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    fields = ["last_name", "email"]
    search_fields = ["email"]


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    date_hierarchy = "publication_date"
    list_display = ["title", display_book_authors, "publisher", "publication_date"]
    actions = [make_book_pub_date_to_now]


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    pass




