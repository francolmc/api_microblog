from django_filters import rest_framework as filters
from .models import Post

class PostFilter(filters.FilterSet):
    content = filters.CharFilter(lookup_expr='icontains')
    created_at_after = filters.DateFilter(field_name='created_at', lookup_expr='gte')
    created_at_before = filters.DateFilter(field_name='created_at', lookup_expr='lte')

    class Meta:
        model = Post
        fields = ['content', 'created_at_after', 'created_at_before']
