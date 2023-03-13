from rest_framework.serializers import ModelSerializer
from mytig.models import ProduitEnPromotion
from mytig.models import AvailableProduct

class ProduitEnPromotionSerializer(ModelSerializer):
    class Meta:
        model = ProduitEnPromotion
        fields = ('id', 'tigID')
        
class AvailableProductSerializer(ModelSerializer):
    class Meta:
        model = AvailableProduct
        fields = ('id', 'tigID')        
