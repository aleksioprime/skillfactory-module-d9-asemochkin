from posts.models import Post, Category
from rest_framework import serializers
from django.contrib.auth.models import User  
from django.utils import timezone 

class AuthorSerializer(serializers.ModelSerializer):  
    class Meta:  
        model = User  
        fields = ['username', 'first_name', 'last_name']

class CatSerializer(serializers.ModelSerializer):  
    posts = serializers.StringRelatedField(many=True, read_only=True)  
    class Meta:  
        model = Category  
        fields = ['id','name', 'posts']

class PostViewSerializer(serializers.ModelSerializer):  
    author = AuthorSerializer(required=False)
    category = serializers.StringRelatedField(read_only=True)  
    class Meta:  
        model = Post  
        fields = ['title', 'content', 'status', 'updated', 'category', 'author']

class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255)  
    status = serializers.CharField(max_length=10)  
    content = serializers.CharField()
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all()) 
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    def create(self, validated_data):
        return Post.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.status = validated_data.get('status', instance.status)
        instance.content = validated_data.get('content', instance.content)
        instance.updated = timezone.now
        instance.category = validated_data.get('category', instance.category)
        instance.author = validated_data.get('author', instance.author)
        instance.save()
        return instance

class CatDetailSerializer(serializers.ModelSerializer):  
    posts = PostViewSerializer(many=True)  
    class Meta:  
        model = Category  
        fields = ['name', 'posts']