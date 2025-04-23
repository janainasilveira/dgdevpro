from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Post
from django.utils import timezone
from .forms import PostForm

# View é tudo aquilo que recebe uma request e retorna uma response
# Create your views here.

def post_list(request):
    # da tabela posts, filtra os objetos que tem a data de publicação maior do que o momeno de agora (timezone.now()), ordenado pela data de publicação.
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

    return render(request, 'blog/post_list.html', {"posts": posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def portao(request):
    return render(request, 'blog/porta.html', {})

#def portao(request):
  #  return HttpResponse("Você chegou ao portão da casa")

def sala(request):
    return HttpResponse("Você chegou na sala")

def quarto(request):
    return HttpResponse("Você chegou no quarto")
