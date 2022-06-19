from django.shortcuts import render,get_object_or_404,redirect
from .models import Post,Category
from django.views.generic import ListView
from .forms import PostSearchForm
from django.db.models import Q 
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

@login_required(login_url='account:register')
def viewupload(request):
    yourposts=Post.newmanager.all().filter(author=request.user.id)

    return render(request, 'blog/viewupload.html',{'yourposts': yourposts})


@login_required(login_url='account:register')
def viewdraft(request):
    query=Q()
    query &= Q(author=request.user.id)
    query &= Q(draft_status='D')
    draftposts = Post.objects.filter(query)

    

    return render(request, 'blog/viewdraft.html',{'draftposts': draftposts})

@login_required(login_url='account:register')
def upload(request):
    category_list = Category.objects.exclude(name='default')
    if request.method == 'POST':
        author=request.user
        title=request.POST['title']
        category=request.POST['categoryselect']
        if request.FILES.get('image') == None:
            messages.info(request,'please upload a image ')
        if request.FILES.get('image') != None:
            postimg =request.FILES.get('image')
        summary=request.POST['summary']
        content=request.POST['content']
        slug=request.POST['slug']
        publish=request.POST['publish']
        draft=request.POST['draft']
        if publish == '' and draft == '':
            messages.info(request,'you should enter P or D dont leave these sections empty')
            return redirect('blog:upload')
        
        post = Post.objects.create( title=title,author=author,postimg=postimg,summary=summary,content=content,slug=slug,publish_status=publish,draft_status=draft
                )
        post.save()
        entry = Post.objects.get(title=title)
        cat_blog = Category.objects.get(name=category)
        entry.category=cat_blog
        entry.save()
        messages.info(request,'you post uploaded successfully')
        return redirect('blog:viewupload')




       
  
    return render(request, "blog/upload.html",{'category_list':category_list})


   
def index(request):
   
    allposts = Post.newmanager.all()
    return render(request,'blog/blogindex.html',{'allposts':allposts})



def post_single(request, post):
    post = get_object_or_404(Post, slug=post, publish_status='P')
    
    return render(request, 'blog/single.html', {'post': post })



class CatListView(ListView):
    template_name = 'blog/category.html'
    context_object_name = 'catlist'
   
    def get_queryset(self):
        content = {
            'cat': self.kwargs['category'],
            'posts': Post.objects.filter(category__name=self.kwargs['category']).filter(publish_status='P'),
           
        }
        return content



def post_search(request):
    form = PostSearchForm()
    c=''
    
    results=[]
    query=Q()
    if "c" in request.GET:
        form=PostSearchForm(request.GET)
        form.full_clean()
        if form.is_valid():
           
            c=form.cleaned_data['c']
            if c is not None:
                query &= Q(category=c)
                
                

    results = Post.newmanager.filter(query)
    return render(request,'blog/search.html',
           {'form':form,'c':c,'results':results}
           )    