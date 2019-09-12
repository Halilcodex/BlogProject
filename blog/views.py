from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from blog.models import Post, Comment
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from blog.forms import PostForm, CommentForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

# Create your views here.
class IndexView(TemplateView):
    template_name = "index.html"


class AboutView(TemplateView):
    template_name = "blog/about.html"


class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"

    def get_queryset(self):
        return Post.objects.filter(post_publish_date__lte=timezone.now()).order_by('-post_publish_date')


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_details.html"

class PostCreateView(CreateView,LoginRequiredMixin):
    login_url = '/login'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post

class PostUpdateView(UpdateView,LoginRequiredMixin):
    login_url = '/login'
    redirect_field_name = 'blog/post_details.html'
    form_class = PostForm
    model = Post

class PostDeleteView(DeleteView,LoginRequiredMixin):
    model = Post

    success_url = reverse_lazy("post_list")

class DraftListView(ListView,LoginRequiredMixin):
    model = Post
    template_name = "blog/post_draft_list.html"
    login_url = '/login'
    redirect_field_name="blog/post_draft_list.html"

    def get_queryset(self):
        return Post.objects.filter(post_publish_date__isnull = True).order_by('-post_create_date')
    

#--Other sub-views(publish,comment,remove comment,approve comment--#

@login_required
def publish_post(request,pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

def add_comment(request,pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        comment_form = CommentForm()
    return render(request, 'blog/comment_form.html',{'form':comment_form})

@login_required
def approve_comment_view(request,pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve_comment()
    return redirect('post_detail', pk =comment.post.pk)

@login_required
def remove_comment(request,pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)
