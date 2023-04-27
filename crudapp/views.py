from rest_framework.viewsets import ModelViewSet
from crudapp.models import Product
from crudapp.serializers import ProductSerializer

# Create your views here.
class Products(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


