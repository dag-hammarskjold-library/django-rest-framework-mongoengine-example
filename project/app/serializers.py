from rest_framework_mongoengine import serializers as mongoserializers

from app.models import UNDocument


class UNDocumentSerializer(mongoserializers.DocumentSerializer):

    class Meta:
        model = UNDocument
        fields = '__all__'
