from blog.models import Post
from django.db.models import Q
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class ListObjectsView(ListView):
    model = Post
    template_name = 'main.html'
    context_object_name = 'posts'


class DetailObjectsView(DetailView):
    model = Post
    template_name = 'detail.html'
    context_object_name = 'post'


class SearchResultsView(ListView):
    model = Post
    template_name = 'search_results.html'
    context_object_name = 'post'

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = Post.objects.filter(Q(title__icontains=query))
        return object_list


class NeedUpdateView(UpdateView):
    model = Post
    template_name = 'edit.html'
    fields = 'title', 'ingredients', 'description'
    success_url = '/'


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = '/'


class PostCreateView(CreateView):
    model = Post
    template_name = 'create.html'
    fields = ['title', 'ingredients', 'description', 'image']
    success_url = '/'
    