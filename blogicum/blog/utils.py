from django.utils.timezone import now

from .models import Post


def get_published_posts(category=None):
    return Post.objects.filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=now(),
    ).order_by('-pub_date')
