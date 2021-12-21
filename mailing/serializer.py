from rest_framework import serializers

from mailing.models import Contact


class MailingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
