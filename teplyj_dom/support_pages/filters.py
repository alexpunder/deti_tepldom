import django_filters
from blog.models import Blog
from django.db.models import Q
from schooling.models import Project


class SearchBlogFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method='filter_by_multiple_fields')

    class Meta:
        model = Blog
        fields = ['search']

    def filter_by_multiple_fields(self, queryset, name, value):
        return queryset.filter(
            Q(title__icontains=value)
            | Q(text__icontains=value)
            | Q(category__name__icontains=value)
        )


class SearchProjectFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method='filter_by_multiple_fields')

    class Meta:
        model = Project
        fields = ['search']

    def filter_by_multiple_fields(self, queryset, name, value):
        return queryset.filter(
            Q(title__icontains=value)
            | Q(short_description__icontains=value)
            | Q(text__icontains=value)
        )
