from .models import *
from django.db.models import Count


def getCatePost(request):
    cate_posts=Post.objects.values('category__cname','category').annotate(c=Count('*')).order_by("-c")
    from django.db import connection
    cursor = connection.cursor()
    datas=cursor.execute("select created,count('*') as count from post group by strftime('%Y-%m',created) order by count desc")
    recent_post=Post.objects.all().order_by("-created")[:3]

    return {"cate_posts":cate_posts,"datas":datas,"recent":recent_post}