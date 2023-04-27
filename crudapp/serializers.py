from rest_framework import serializers
from crudapp.models import Category, Product

class CategorySerializer(serializers.ModelSerializer):
    fields = '__all__'
    model = Category

class ProductSerializer(serializers.ModelSerializer):    
    category_name = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = ['id', 'title','price','image', 'description', 'category', 'category_name']

    def get_category_name(self, obj):
        return obj.category.title