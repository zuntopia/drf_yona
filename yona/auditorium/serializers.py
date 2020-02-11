from rest_framework import serializers
from auditorium.models import GitHubEye

class GitHubSerializer(serializers.Serializer):
    id: serializers.IntegerField(read_only=True)

    def create(self, validate_data):
        return GitHubEye.objects.create(**validate_data)
