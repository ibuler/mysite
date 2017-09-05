from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse

from .forms import PublisherForm
from .models import Publisher


# def publisher_add(request):
#     if request.method == "POST":
#         form = PublisherForm(request.POST)
#         if form.is_valid():
#             publisher = Publisher(
#                 name=form.cleaned_data["name"],
#                 address=form.cleaned_data["address"],
#                 state_province=form.cleaned_data["state_province"],
#                 country=form.cleaned_data["country"],
#                 website=form.cleaned_data["website"])
#             publisher.save()
#             return HttpResponse("添加成功")
#             # return redirect("/publisher/{pk}/detail".format(pk=publisher.pk))
#         else:
#             return render(request, "books/publisher_add.html", {"form": form})
#     else:
#         form = PublisherForm()
#         return render(request, "books/publisher_add.html", {"form": form})


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