from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post
from django.views.generic import TemplateView


def home(request) -> HttpResponse:
    context = {
        'posts': Post.objects.all()
    }
    return render(request,'blog/home.html', context)

class About(TemplateView):
    template_name = 'blog/about.html'


