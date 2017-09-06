from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.views.generic import TemplateView


class AboutView(TemplateView):
    template_name = "about.html"


class MyView(View):
    def get(self, request):
        return render(request, "view.html")

    def post(self, request):
        # <view logic>
        return HttpResponse('post it')

    def head(self, request):
        # <view logic>
        return HttpResponse('head it')