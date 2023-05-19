from django.shortcuts import render, redirect, reverse
from .forms import PostForm
from taggit.models import Tag
from .models import Post, Category
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .filters import PostFilter
from django.db.models import Count


def blog(request):
    blogs = Post.objects.all().order_by('-published_at')
    posts = blogs[:3]
    category = (Category.objects.annotate(post_count=Count('post_category')))[:6]
    
    # filter
    filter = PostFilter(request.GET, queryset=blogs)
    blogs = filter.qs
    
    # pagination 
    paginator = Paginator(blogs, 4) # Show 4 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
        
    context = {'posts': posts, 'blog': page_obj, 'search': filter, 'category': category}
    return render(request, 'blog.html', context)


@login_required
def add_post(request):
    # show most common tags
    commonTags = Post.tags.most_common()[:4]
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            myForm = form.save(commit=False)
            myForm.author = request.user
            myForm.save()
            form.save_m2m()
            return redirect(reverse('blog:blog'))
    else:
        form = PostForm()
    
    context = {'form': form}
    return render(request, 'add_post.html', context)


def post_details(request, slug):
    post = Post.objects.get(slug=slug)
    context = {'post': post}
    return render(request, 'single_blog.html', context)


def display_category(request, name):
    posts = Post.objects.filter(category__name=name)
    category = (Category.objects.annotate(post_count=Count('post_category')))[:6]
    context = {'posts': posts, 'category': category}
    return render(request, 'category_posts.html', context)