from django.conf.urls import url

from post import views

urlpatterns=[
    url(r"^content/(\d+)$",views.details_view),
    url(r"^page/(\d+)$",views.index_view),
    url(r"^cate/(\d+)",views.get_post_cate),
    url(r"date/(\d+)/(\d+)",views.get_post_by_date),
    url(r'^search/$',views.search_view),
    url(r"^aboutme",views.about_views),
    url(r"",views.index_view)
]