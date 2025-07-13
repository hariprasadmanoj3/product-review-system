from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)
    average_rating = serializers.ReadOnlyField()
    review_count = serializers.ReadOnlyField()

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'description', 'price', 'created_by',
            'created_at', 'updated_at', 'average_rating', 'review_count'
        ]
        read_only_fields = ['id', 'created_by', 'created_at', 'updated_at']

    def create(self, validated_data):
        validated_data['created_by'] = self.context['request'].user
        return super().create(validated_data)

class ProductDetailSerializer(ProductSerializer):
    reviews = serializers.SerializerMethodField()

    class Meta(ProductSerializer.Meta):
        fields = ProductSerializer.Meta.fields + ['reviews']

    def get_reviews(self, obj):
        from reviews.serializers import ReviewSerializer
        reviews = obj.reviews.all()[:10]  # Limit to 10 recent reviews
        return ReviewSerializer(reviews, many=True).data