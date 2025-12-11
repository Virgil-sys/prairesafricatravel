from rest_framework import serializers
from .models import Testimonial

class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = ['id', 'name', 'location', 'message', 'rating', 'created_at']
        read_only_fields = ['id', 'created_at']

    def create(self, validated_data):
        # Set is_approved to False for new testimonials (they need admin approval)
        validated_data['is_approved'] = False
        return super().create(validated_data)
