from django.shortcuts import render,get_object_or_404
from .models import Post,Category
from django.views.generic import ListView
from .forms import PostSearchForm
from django.db.models import Q 
# Create your views here.
def index(request):
    allposts = Post.objects.all().filter(status='published')
    return render(request,'blog/blogindex.html',{'allposts':allposts})



def post_single(request, post):
    post = get_object_or_404(Post, slug=post, status='published')
    category_list = Category.objects.exclude(name='default')
    return render(request, 'blog/single.html', {'post': post })



class CatListView(ListView):
    template_name = 'blog/category.html'
    context_object_name = 'catlist'
   
    def get_queryset(self):
        content = {
            'cat': self.kwargs['category'],
            'posts': Post.objects.filter(category__name=self.kwargs['category']).filter(status='published'),
           
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
                

    results = Post.objects.filter(query)
    return render(request,'blog/search.html',
           {'form':form,'c':c,'results':results}
           )    