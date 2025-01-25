from django.shortcuts import get_object_or_404, render
from django.utils.timezone import now

from .models import Post, Category

from blogicum.settings import MAX_POSTS_PER_PAGE


def get_published_posts(category=None):
    return Post.objects.filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=now(),
    ).order_by('-pub_date')


def index(request):
    posts = get_published_posts().filter(category__is_published=True
                                         )[:MAX_POSTS_PER_PAGE]
    return render(request, 'blog/index.html', {'posts': posts})


def post_detail(request, post_id):
    post = get_object_or_404(
        Post,
        id=post_id,
        is_published=True,
        category__is_published=True,
        pub_date__lte=now(),
    )
    return render(request, 'blog/detail.html', {'post': post})


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True,
    )
    posts = get_published_posts().filter(category=category)
    context = {
        'category': category,
        'post_list': posts,
    }
    return render(request, 'blog/category.html', context)
