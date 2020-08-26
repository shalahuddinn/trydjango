from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView


# Create your views here.
from .forms import ArticleForm
from .models import Article


class ArticleListView(ListView):
    # template_name = 'articles/article_list.html'
    queryset = Article.objects.all()  # blog/<modelname>_list.html


class ArticleDetailView(DetailView):
    # template_name = 'articles/article_detail.html'
    # queryset = Article.objects.all()  # blog/<modelname>_list.html

    def get_object(self, queryset=None):
        id = self.kwargs.get('id')
        return get_object_or_404(Article, id=id)

    
class ArticleCreateView(CreateView):
    template_name = 'blog/article_create.html'
    form_class = ArticleForm
    queryset = Article.objects.all()  # blog/<modelname>_list.html
    success_url = '/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    # def get_success_url(self):
    #     return '/'


class ArticleUpdateView(UpdateView):
    template_name = 'blog/article_create.html'
    form_class = ArticleForm
    queryset = Article.objects.all()  # blog/<modelname>_list.html
    success_url = '/'

    def get_object(self, queryset=None):
        id = self.kwargs.get('id')
        return get_object_or_404(Article, id=id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    # def get_success_url(self):
    #     return '/'


class ArticleDeleteView(DeleteView):
    template_name = 'blog/article_delete.html'

    def get_object(self, queryset=None):
        id = self.kwargs.get('id')
        return get_object_or_404(Article, id=id)

    def get_success_url(self):
        return reverse('blog:article-list')
