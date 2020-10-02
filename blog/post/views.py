from django.shortcuts import render
from post.models import Post
from django.core.paginator import Paginator


def get_post_by_num(num):
    num = int(num)
    posts = Post.objects.all().order_by("-created")
    paginator = Paginator(posts,per_page=1)
    if num < 1:
        num = 1
    if num > paginator.num_pages:
        num = paginator.num_pages
    start = int(((num-1)/10)*10+1)
    end = num+3
    if end > paginator.num_pages:
        end = paginator.num_pages+1
    return paginator.page(num), range(start,end)


def index_view(request, num="1"):
    page_posts,page_range=get_post_by_num(num)
    return render(request, "index.html", {"posts": page_posts, "page_range": page_range})


def details_view(request, post_id):
    post_id = int(post_id)
    post = Post.objects.get(id=post_id)
    return render(request, "detail.html", {"post":post})


def get_post_cate(request,cate_id):
    cate_id = int(cate_id)
    cates = Post.objects.filter(category_id=cate_id)
    return render(request, "category.html", {"cates": cates})


def get_post_by_date(request, year, month):
    date_posts = Post.objects.filter(created__year=year, created__month=month)
    return render(request, "category.html", {"cates": date_posts})


# 全文搜索功能
def search_view(request):
    from haystack.query import SearchQuerySet
    from haystack.query import SQ
    # 获取请求参数
    keywords = request.GET.get('q','')
    search_posts = SearchQuerySet().filter(SQ(title=keywords)|SQ(content=keywords))
    s_posts = []
    for s_p in search_posts:
        s_posts.append(s_p.object)
    return render(request, 'category.html', {'cates': s_posts})


def about_views(request):
    return render(request,'about.html')