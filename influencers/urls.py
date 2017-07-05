from django.conf.urls import url
from .views import SearchTagAPI


urlpatterns = [
    url(r'^tags/$', SearchTagAPI.as_view({
        'post': 'tag', 
    }), name="tag_search"),
]
