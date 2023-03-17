import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from mytig.config import baseUrl
from mytig.models import InfoProduct
from mytig.serializers import InfoProductSerializer
from rest_framework_simplejwt.tokens import AccessToken
from django.contrib.auth.models import User

##response = requests.post('http://127.0.0.1:8000/api/token/', data={'username': 'eric', 'password': 'eric123'})
##token = response.json()['access']

##headers = {'Authorization': 'Bearer ' + token}
##response = requests.get('http://127.0.0.1:8000/infoproducts/', headers=headers)
#######################
#...JWT début...#
from rest_framework.permissions import IsAuthenticated
#...JWT fin...#
#######################
class InfoProductList(APIView):
#######################
#...TME3 JWT starts...#
    permission_classes = (IsAuthenticated,)
#...end of TME3 JWT...#
#######################
def get(self, request, format=None):
    products = InfoProduct.objects.all()
    serializer = InfoProductSerializer(products, many=True)
    return Response(serializer.data)
class InfoProductDetail(APIView):
#######################
#...TME3 JWT starts...#
    permission_classes = (IsAuthenticated,)
#...end of TME3 JWT...#
#######################

# Create your views here.
class RedirectionListeDeProduits(APIView):
    def get(self, request, format=None):
        response = requests.get(baseUrl+'products/')
        jsondata = response.json()
        return Response(jsondata)
#    def post(self, request, format=None):
#        NO DEFITION of post --> server will return "405 NOT ALLOWED"

class RedirectionDetailProduit(APIView):
    def get(self, request, pk, format=None):
        try:
            response = requests.get(baseUrl+'product/'+str(pk)+'/')
            jsondata = response.json()
            return Response(jsondata)
        except:
            raise Http404
#    def put(self, request, pk, format=None):
#        NO DEFITION of put --> server will return "405 NOT ALLOWED"
#    def delete(self, request, pk, format=None):
#        NO DEFITION of delete --> server will return "405 NOT ALLOWED"

class RedirectionShipPoints(APIView):
    def get(self, request, format=None):
        response = requests.get(baseUrl+'shipPoints/')
        jsondata = response.json()
        return Response(jsondata)

class RedirectionShipPointDetails(APIView):
    def get(self, request, pk, format=None):
        try:
            response = requests.get(baseUrl+'shipPoint/'+str(pk)+'/')
            jsondata = response.json()
            return Response(jsondata)
        except:
            raise Http404
class UpdateProductStock(APIView):
    def put(self, request, pk, format=None):
        try:
            product_data = request.data
            response = requests.put(baseUrl + f'product/{pk}/', json=product_data)
            jsondata = response.json()
            return Response(jsondata, status=status.HTTP_200_OK)
        except:
            raise Http404

from mytig.models import ProduitEnPromotion, AvailableProduct
from mytig.serializers import ProduitEnPromotionSerializer, AvailableProductSerializer
from django.http import Http404
from django.http import JsonResponse

class PromoList(APIView):
    def get(self, request, format=None):
        res=[]
        for prod in ProduitEnPromotion.objects.all():
            serializer = ProduitEnPromotionSerializer(prod)
            response = requests.get(baseUrl+'product/'+str(serializer.data['tigID'])+'/')
            jsondata = response.json()
            res.append(jsondata)
        return JsonResponse(res, safe=False)
#    def post(self, request, format=None):
#        NO DEFITION of post --> server will return "405 NOT ALLOWED"

class PromoDetail(APIView):
    def get_object(self, pk):
        try:
            return ProduitEnPromotion.objects.get(pk=pk)
        except ProduitEnPromotion.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        prod = self.get_object(pk)
        serializer = ProduitEnPromotionSerializer(prod)
        response = requests.get(baseUrl+'product/'+str(serializer.data['tigID'])+'/')
        jsondata = response.json()
        return Response(jsondata)
#    def put(self, request, pk, format=None):
#        NO DEFITION of put --> server will return "405 NOT ALLOWED"
#    def delete(self, request, pk, format=None):
#        NO DEFITION of delete --> server will return "405 NOT ALLOWED"

class AvailableList(APIView):
    def get(self, request, format=None):
        res=[]
        for prod in AvailableProduct.objects.all():
            serializer = AvailableProductSerializer(prod)
            response = requests.get(baseUrl+'product/'+str(serializer.data['tigID'])+'/')
            jsondata = response.json()
            res.append(jsondata)
        return JsonResponse(res, safe=False)
    
class AvailableDetail(APIView):
    def get_object(self, pk):
        try:
            return AvailableProduct.objects.get(pk=pk)
        except AvailableProduct.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        prod = self.get_object(pk)
        serializer = AvailableProductSerializer(prod)
        response = requests.get(baseUrl+'product/'+str(serializer.data['tigID'])+'/')
        jsondata = response.json()
        return Response(jsondata)
#    def put(self, request, pk, format=None):
#        NO DEFITION of put --> server will return "405 NOT ALLOWED"
#    def delete(self, request, pk, format=None):
#        NO DEFITION of delete --> server will return "405 NOT ALLOWED"

