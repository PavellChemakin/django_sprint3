from django.shortcuts import get_object_or_404, render
from django.utils.timezone import now
from .models import Post, Category


def index(request):
    posts = Post.objects.filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=now()
    ).order_by('-pub_date')[:5]
    return render(request, 'blog/index.html', {'posts': posts})


def post_detail(request, id):
    post = get_object_or_404(
        Post,
        id=id,
        is_published=True,
        category__is_published=True,
        pub_date__lte=now()
    )
    return render(request, 'blog/detail.html', {'post': post})


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    posts = Post.objects.filter(
        category=category,
        is_published=True,
        pub_date__lte=now()
    ).order_by('-pub_date')
    context = {
        'category': category,
        'post_list': posts
    }
    return render(request, 'blog/category.html', context)
