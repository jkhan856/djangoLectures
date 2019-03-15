from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from blog import models
from django.urls import reverse_lazy
from blog.forms import PostForm, CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.contrib.auth.decorators import login_required

class IndexView(TemplateView):
    template_name = 'index.html'

class AboutView(TemplateView):
    template_name = 'about.html'

class PostListView(ListView):
    #context_object_name = 'posts'
    model = models.Post

    def get_queryset(self):
        return models.Post.objects.filter(published_date__lte = timezone.now()).order_by('-published_date')

class PostDetailView(DetailView):
    model = models.Post
    #context_object_name = 'post_detail'

class CreatePostView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = models.Post

class PostUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = models.Post

class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = models.Post
    success_url = reverse_lazy('blog:post_list')

class DraftListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_list.html'
    model = models.Post

    def get_queryset(self):
        return models.Post.objects.filter(published_date__isnull = True).order_by('created_date')


################################################
#Comment Section

@login_required
def post_publish(request, pk):
    post = get_object_or_404(models.Post, pk = pk)
    post.publish()
    return redirect("blog:post_detail", pk = pk)


@login_required
def add_comment_to_post(request,pk):
    post = get_object_or_404(models.Post, pk=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit = False)
            comment.post = post
            comment.save()
            return redirect("blog:post_detail",pk = post.pk)
    else:
        form= CommentForm()
    return render(request, 'blog/comment_form.html', {'form':form})


#######
#Approve a Comment

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(models.Comment,pk = pk)
    comment.approve()
    return redirect("blog:post_detail", pk = comment.post.pk)

######Remove CommentForm

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(models.Comment,pk = pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect("blog:post_detail", pk = post_pk)
