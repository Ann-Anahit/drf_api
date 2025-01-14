from rest_framework import serializers
from posts.models import Post
from likes.models import Like
from category.models import PostCategory

class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    like_id = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()
    category = serializers.SerializerMethodField()

    class PostSerializer(serializers.ModelSerializer):
        category = serializers.SerializerMethodField()

    def get_category(self, obj):
        print(f"Category for Post {obj.id}: {obj.category}") 
        if obj.category:
            print(f"Category name: {obj.category.name}, image: {obj.category.image.url if obj.category.image else None}")
        return {
            "id": obj.category.id if obj.category else None,
            "name": obj.category.name if obj.category else None,
            "image": obj.category.image.url if obj.category and obj.category.image else None,
        } if obj.category else None

    class Meta:
        model = Post
        fields = ['id', 'title', 'category']

    def validate_image(self, value):
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError('Image size larger than 2MB!')
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px!'
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(
                owner=user, post=obj
            ).first()
            return like.id if like else None
        return None

    class Meta:
        model = Post
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'created_at', 'updated_at',
            'title', 'content', 'image', 'image_filter',
            'like_id', 'likes_count', 'comments_count',
            'category',
        ]
