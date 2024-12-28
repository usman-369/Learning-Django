from rest_framework import serializers
from .models import ContactBook


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactBook
        fields = ['id', 'firstname', 'lastname', 'phone', 'email']
