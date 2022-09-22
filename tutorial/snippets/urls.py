from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from snippets.views import *

urlpatterns = [
    path('snippets/', snippet_list),
    path('snippets/<int:pk>/', snippet_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
