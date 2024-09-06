from rest_framework import serializers
from .models import *


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name']

class BlogTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blogs
        fields = '__all__'


class BlogsSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    class Meta:
        model = Blogs
        fields = '__all__'



class BlogSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    related_blogs = serializers.SerializerMethodField()

    class Meta:
        model = Blogs
        fields = ['slug', 'title', 'image', 'logo', 'description', 'tags', 'related_blogs']

    def get_related_blogs(self, obj):
        # Get all tags for the current blog
        tags = obj.tags.all()
        # Find related blogs that share at least one tag with the current blog
        related_blogs = Blogs.objects.filter(tags__in=tags).exclude(id=obj.id).distinct()
        return BlogSerializer(related_blogs, many=True).data


class BloggSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = Blogs
        fields = ['slug', 'title', 'image', 'logo', 'description', 'tags', 'is_popular']

    def create(self, validated_data):
        tags_data = validated_data.pop('tags', [])
        blog = Blogs.objects.create(**validated_data)
        
        for tag_data in tags_data:
            tag, _ = Tag.objects.get_or_create(name=tag_data['name'])
            blog.tags.add(tag)
        
        return blog

    def update(self, instance, validated_data):
        tags_data = validated_data.pop('tags', [])
        
        instance.slug = validated_data.get('slug', instance.slug)
        instance.title = validated_data.get('title', instance.title)
        instance.image = validated_data.get('image', instance.image)
        instance.logo = validated_data.get('logo', instance.logo)
        instance.description = validated_data.get('description', instance.description)
        
        instance.save()

        # Update tags
        instance.tags.clear()
        for tag_data in tags_data:
            tag, _ = Tag.objects.get_or_create(name=tag_data['name'])
            instance.tags.add(tag)
        
        return instance
    

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class PopularTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name']



class TagsSerializer(serializers.ModelSerializer):
    blogs=BlogTagSerializer()
    class Meta:
        model = Tag
        fields = ['name', 'blogs', 'slug']


class CategoriesSerializer(serializers.ModelSerializer):
    blogs=BlogTagSerializer()
    class Meta:
        model = Category
        fields = ['name', 'blogs','slug']
