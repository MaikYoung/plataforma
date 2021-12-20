from rest_framework import serializers

from mailing.models import Contact


class MailingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

    def create(self, validated_data):
        contact = Contact(**validated_data)
        return contact
