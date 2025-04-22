from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.utils import timezone

# View é tudo aquilo que recebe uma request e retorna uma response
# Create your views here.

def post_list(request):
    # da tabela posts, filtra os objetos que tem a data de publicação maior do que o momeno de agora (timezone.now()), ordenado pela data de publicação.
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

    return render(request, 'blog/post_list.html', {"posts": posts})

def portao(request):
    return render(request, 'blog/porta.html', {})

#def portao(request):
  #  return HttpResponse("Você chegou ao portão da casa")

def sala(request):
    return HttpResponse("Você chegou na sala")

def quarto(request):
    return HttpResponse("Você chegou no quarto")
