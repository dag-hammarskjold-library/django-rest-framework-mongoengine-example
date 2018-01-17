from rest_framework_mongoengine import serializers as mongoserializers

from app.models import UNDocument, Blog
from rest_framework_elasticsearch.es_serializer import ElasticModelSerializer
from .search_indexes import BlogIndex


class UNDocumentSerializer(mongoserializers.DocumentSerializer):
    class Meta:
        model = UNDocument
        fields = '__all__'


class BlogSerializer(mongoserializers.DocumentSerializer):
    class Meta:
        model = Blog
        fields = '__all__'


class ElasticBlogSerializer(ElasticModelSerializer):
    class Meta:
        model = Blog
        es_model = BlogIndex
        fields = ('pk', 'title', 'created_at', 'tags', 'body', 'is_published')
