from rest_framework import serializers
from news.models import Article


class ArticleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    author = serializers.CharField(max_length=50)
    title = serializers.CharField(max_length=120)
    description = serializers.CharField(max_length=200)
    body = serializers.CharField()
    location = serializers.CharField(max_length=120)
    pub_date = serializers.DateField()
    is_active = serializers.BooleanField()
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        print(validated_data)
        return Article.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.author = validated_data.get('author', instance.author)
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.body = validated_data.get('body', instance.body)
        instance.location = validated_data.get('location', instance.location)
        instance.pub_date = validated_data.get('pub_date', instance.pub_date)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.save()
        return instance