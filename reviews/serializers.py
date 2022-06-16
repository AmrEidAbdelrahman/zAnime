from rest_framework import serializers

from reviews.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = ('id', 'content', 'user', 'created_at')

    def get_user(self, obj):
        return obj.user.username