from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .forms import PublisherForm
from .models import Publisher, Book, Author


def publisher_add(request):
    if request.method == 'POST':
        form = PublisherForm(request.POST)
        if form.is_valid():
            publisher = form.save()
            return HttpResponse('Add success')
            #return redirect('some view name')
    else:
        form = PublisherForm(initial={"city": "北京"})

    return render(request, 'books/publisher_add.html', {'form': form})


def publisher_update(request, publisher_id):
    publisher = get_object_or_404(Publisher, id=publisher_id)

    if request.method == 'POST':
        form = PublisherForm(request.POST, instance=publisher)
        if form.is_valid():
            publisher = form.save()
            return HttpResponse('Update success')

    form = PublisherForm(instance=publisher)
    return render(request, 'books/publisher_add.html', {'form': form})


class PublisherList(ListView):
    model = Publisher
    queryset = Publisher.objects.all()
    context_object_name = 'publishers'
    template_name = 'books/publisher_list.html'

    def get_queryset(self):
        return Publisher.objects.all()


class PublisherDetail(DetailView):
    model = Publisher
    content_object_name = 'publisher'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PublisherDetail, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['book_list'] = Book.objects.all()
        return context

    # def get_object(self):
    #     object = super(PublisherDetail, self).get_object()
    #     object.last_accessed = timezone.now()
    #     object.save()
    #     return object


class AuthorList(ListView):
    model = Author


class AuthorDetail(DetailView):
    model = Author


class AuthorCreate(SuccessMessageMixin, CreateView):
    model = Author
    fields = ['first_name', 'last_name', 'email']
    # form_class = forms.AuthorCreateForm
    template_name = 'books/author_form.html'
    success_url = reverse_lazy('books:author-list')
    success_message = "<a href='{url}'> {name} </a>  was created successfully"
    #
    # def form_valid(self, form):
    #     # do_something()
    #     return super().form_valid(form)
    #
    #     # def form_invalid(self, form):
    #     # do_something()
    #     # return super().form_invalid(form)
    #
    # def get_context_data(self, **kwargs):
    #     context = {
    #         "extra": "some context",
    #     }
    #     kwargs.update(context)
    #     return super().get_context_data(**kwargs)

    def get_success_message(self, cleaned_data):
        url = reverse_lazy('books:author-detail', kwargs={'pk': self.object.pk})
        return self.success_message.format(
            url=url, name=self.object.last_name
        )


class AuthorUpdate(SuccessMessageMixin, UpdateView):
    model = Author
    fields = "__all__"
    success_url = reverse_lazy("books:author-list")
    success_message = "%(first_name)s %(last_name)s was update successfully"


class AuthorDelete(DeleteView):
    model = Author
    success_url = reverse_lazy("books:author-list")

