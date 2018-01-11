from django.template.response import TemplateResponse

from rest_framework_mongoengine.viewsets import ModelViewSet as MongoModelViewSet

from app.serializers import UNDocumentSerializer
from app.models import UNDocument


def index_view(request):
    context = {}
    return TemplateResponse(request, 'index.html', context)


class UNDocumentViewSet(MongoModelViewSet):
    lookup_field = 'id'
    serializer_class = UNDocumentSerializer

    def get_queryset(self):
        return UNDocument.objects.all()
