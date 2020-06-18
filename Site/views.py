from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError
from .models import Post, Comment, Reply
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .import forms
from.forms import CommentForm, FeedbackForm
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.
def home(request):
    content = Post.objects.all()   # variable content is first 50 posts in Post model
    form = forms.FeedbackForm() # so that feedbackform can be displayed on home page
    paginator = Paginator(content, 50)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)
    if page.has_next():
        next_link = f'?page={page.next_page_number()}'
    else:
        next_link =''
    if page.has_previous():
        prev_link = f'?page={page.previous_page_number()}'
    else:
        prev_link = ''
    old = Post.objects.all()[51:81] #this will get all old posts from db. note that is this old is defined outsite this function it wont work DRY

    #for my search bar
    query = ""
    if request.GET:
        query = request.GET('q')
    context = {'contents': page, 'form':form, 'next_page_url':next_link, 'prev_page_url':prev_link, 'old':old, 'query':str(query)}
    return render(request, 'site/home.html', context )    #pass a dictionanr of posts and form in the home page



def post_body(request, slug):   # pass a value of request and slug to post body or details
    details = Post.objects.get(slug=slug)
    post = get_object_or_404(Post, slug=slug)   #get post slug from Post model, this slug will get the values of title, user, body... for each post in db
    #replies = get_object_or_404(Comment) so that repkies can be displayed in post body
    #everything here is for commmenting
    form = FeedbackForm()
    comments = post.comments.filter(active=True)
    comment_form = forms.CommentForm()
    if request.method=='POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save( commit = False)    #dont save the form yet in database
            comment.post = post     #assign this comment to this post before saving
            comment.save()
            messages.success(request, "Your Comment is awaiting approval.Thank you")
            return redirect('site:details', slug)   #refresh after saving
    else:
        comment_form = CommentForm()
    context = {'details': details,'comments':comments,'comment_form':comment_form, 'form': form, 'post':post}
    return render(request, 'site/post_body.html', context)


#views for create post form
@login_required(login_url="/profile/login/")
def create_post(request):
    if request.method=='POST':
        form = forms.CreatePost(request.POST, request.FILES)
        if form.is_valid():
            #save post to db
            instance = form.save(commit=False)
            instance.user = request.user #instance.user this user is the one i created as post author in models
            instance.save()
            #save ends
            return redirect('site:home')
    else:
        form = forms.CreatePost()
    return render(request, 'site/create_post.html', {'form': form})


def feedback(request):
    if request.method == 'GET':
            form = forms.FeedbackForm()
    else:
        form = forms.FeedbackForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            #form.save(commit=False)
            try:
                send_mail(subject, message, email,  ['patrickabugu@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Feedback not sent! Try again')
            return redirect('site.home')

    return render(request, 'site/home.html', {'form':form})



@login_required(login_url="/profile/login/")
def editpost(request, slug = None ):
    instance = get_object_or_404(Post, slug=slug)
    if request.user == instance.user:   #check if the user forcing himself to edit the post is the owner that is the user instance
            if request.method == 'POST':
                form = forms.CreatePost(request.POST or None, request.FILES or None, instance = instance)
                context = {'form':form}
                if form.is_valid():
                    obj = form.save(commit=False)
                    obj.save()
                    messages.success(request, "Your post has been successfully updated")
                    context = {'form':form}
                    return render(request, 'site/edited_post.html', context)
                else:
                    context = {'form': form, 'error': "The post was not successfully updated. Try again"}
                    return render(request, 'site/edit_post.html', context)
            else:
                form = forms.CreatePost(request.GET or None, request.FILES or None, instance = instance)
                context = {'form':form}
                return render(request, 'site/edit_post.html', context)
    else:
        return HttpResponse('You are an idiot!\n This is not your post') # if he/seh doesntown the post insult him

@login_required
def deletepost(request, slug = None):
    instance = get_object_or_404(Post, slug=slug)
    if request.user == instance.user:
            instance.delete()
            #return render(request, 'site:deleted.html')
            return HttpResponse('Your post has been deleted successfully!')
    else:
        return HttpResponse('You are an idiot.. This is not your post!')


'''def comment(request, slug = None):
    post = get_object_or_404(Post, slug=slug)
    if request.method=='POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save( commit = False)
            comment.post = post
            comment.save()
            return redirect('site:details', slug)
    else:
        comment_form = CommentForm()
    return render(request, 'site/comments.html', {'comment_form':comment_form})'''




'''def reply(request, slug = None):
    #post = get_object_or_404(Post, slug=slug)
    replies = get_object_or_404(Comment, slug=slug)
    if request.method == 'POST':
        reply_form = ReplyForm(request.POST)
        if form.is_valid():
            reply = ReplyForm.save()
            reply.replies = replies
            reply.save()
            return redirect('site:details', slug)
    else:
        reply_form = ReplyForm()
    return render(request, 'site/comments.html', {'reply_form':reply_form})'''

'''def search(request):
    if request.method == 'GET':
        query = request.GET.get('q')
        submitbutton = request.GET.get('Submit')
        if query is not None:
            lookups = Q(title__icontains=query)|Q(body__icontains=query)
            results = Post.objects.filter(lookups).distinct()
            context = {'results':results, 'submitbutton':submitbutton}
            return render(request, 'site/search.html', context)
        else:
            return render(request, 'site/home.html', context)
    else:
        return render(request, 'site/home.html', context)'''
