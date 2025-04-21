from django.shortcuts import render
from django.http import HttpResponse

# View é tudo aquilo que recebe uma request e retorna uma response
# Create your views here.

def post_list(request):
    return render(request, 'blog/post_list.html', {})

def portao(request):
    return render(request, 'blog/porta.html', {})

#def portao(request):
  #  return HttpResponse("Você chegou ao portão da casa")

def sala(request):
    return HttpResponse("Você chegou na sala")

def quarto(request):
    return HttpResponse("Você chegou no quarto")
