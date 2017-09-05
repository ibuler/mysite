from django import forms

from .models import Author, Book, Publisher


# class PublisherForm(forms.Form):
#     name = forms.CharField(label='Your name',max_length=30)
#     address = forms.CharField(max_length=50, help_text="这是地址")
#     city = forms.CharField(max_length=60)
#     state_province = forms.CharField(max_length=30)
#     country = forms.CharField(max_length=20)
#     website = forms.CharField(max_length=50)


class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = '__all__'
        labels = {
            "name": "姓名",
        }
        help_texts = {
            "name": "姓名是什么?"
        }


# forms.py
class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'email']


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'authors']