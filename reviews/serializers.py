from rest_framework import serializers
from .models import Review
from products.models import Product

class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    product_name = serializers.CharField(source='product.name', read_only=True)

    class Meta:
        model = Review
        fields = [
            'id', 'product', 'product_name', 'user', 'rating', 
            'comment', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'user', 'created_at', 'updated_at']

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

    def validate_product(self, value):
        user = self.context['request'].user
        if Review.objects.filter(product=value, user=user).exists():
            raise serializers.ValidationError(
                "You have already reviewed this product."
            )
        return value