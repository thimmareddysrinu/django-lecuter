from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import (TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView)
from django.urls import reverse_lazy
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from blogapp.forms import PostForm,CommentForm
from .models import Post,Comment
# Create your views here.
class AboutView(TemplateView):
                   template_name='about.html'

class PostListView(ListView):
                   model=Post 

                   def get_queryset(self):
                           return Post.objects.filter(publised_date__Ite=timezone.now()).order_by('-published_date') 
class PostDetailView(DetailView):
                   model=Post                           

class CreatePostVieww(LoginRequiredMixin,CreateView):
                   login_url ='/login/'

                   redirect_field_name='blogapp/post_details.html'
                   form_name=PostForm
                   model=Post                   

class PostUpdateView(LoginRequiredMixin,UpdateView):
                   login_url ='/login/'

                   redirect_field_name='blogapp/post_details.html'
                   form_name=PostForm
                   model=Post                   
class PostDeleteView(LoginRequiredMixin,DeleteView):
                   model=Post
                   success_url=reverse_lazy('post_list')

class DraftListView(ListView,LoginRequiredMixin):
                   login_url='/login/'
                   redirect_field_name='blogapp/post_list.html' 
                   
                                     
                   def  get_queryset(self):
                         return Post.objects.filter(publised_date__isnull=True).order_by('created_date')

######################################
###################################

@login_required
def post_publish(request,pk):
                         post=get_object_or_404(Post,pk=pk)
                         post.publish()
                         return redirect(request,'post_detail',pk=pk)

                         
                  




@login_required
def add_comment_to_post(request,pk):
                         post=get_object_or_404(Post,pk=pk)
                         if request.method =='POST':
                              form=CommentForm(request.post)
                              if form.is_valid():
                                    CommentForm=form.save(commit=False)
                                    Comment.post=post
                                    Comment.save()
                                    return redirect('post_detail',pk=post.pk)
                              else:
                                       form=CommentForm
                                       return render (request,'blogapp/comment_form.html',{'form':form})

def comment_approve(request,pk):
                         comment=get_object_or_404(Comment,pk=pk)
                         comment.approve()
                         return redirect('post_detail',pk=comment.post.pk)

def comment_remove(request,pk):
                         comment=get_object_or_404(Comment,pk=pk)
                         post_pk=comment.post.pk
                         comment.delete()
                         return redirect('post_detail',pk=post_pk)

                             

