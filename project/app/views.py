from django.template.response import TemplateResponse

from rest_framework_mongoengine.viewsets import ModelViewSet as MongoModelViewSet

from app.serializers import UNDocumentSerializer, BlogSerializer
from app.models import UNDocument, Blog
from rest_framework_elasticsearch import es_views, es_client, es_pagination, es_filters
from .search_indexes import BlogIndex


def index_view(request):
    context = {}
    return TemplateResponse(request, 'index.html', context)


class UNDocumentViewSet(MongoModelViewSet):
    lookup_field = 'document_symbol'
    serializer_class = UNDocumentSerializer

    def get_queryset(self):
        return UNDocument.objects.all()


class BlogViewSet(MongoModelViewSet):
    lookup_field = "title"
    serializer_class = BlogSerializer

    def get_queryset(self):
        return Blog.objects.all()


class BlogView(es_views.ListElasticAPIView):
    es_client = es_client
    es_model = BlogIndex
    es_pagination_class = es_pagination.ElasticLimitOffsetPagination
    es_filter_backends = (
        es_filters.ElasticFieldsFilter,
        es_filters.ElasticFieldsRangeFilter,
        es_filters.ElasticSearchFilter,
        es_filters.ElasticOrderingFilter,
    )
    es_ordering = 'created_at'
    es_filter_fields = (
        es_filters.ESFieldFilter('tag', 'tags'),
    )
    es_range_filter_fields = (
        es_filters.ESFieldFilter('created_at', 'created_at'),
    )
    es_search_fields = (
        'tags',
        'title',
    )
