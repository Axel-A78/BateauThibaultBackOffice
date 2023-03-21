import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from mytig.config import baseUrl
from mytig.models import InfoProduct
from mytig.serializers import InfoProductSerializer
from rest_framework import status
from django.http import Http404
from rest_framework_simplejwt.tokens import AccessToken
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from django.core.exceptions import ObjectDoesNotExist
# Ajoutez ces imports si nécessaire
from django.core.exceptions import ValidationError
from .models import InfoProduct
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

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
    def get(self, request, tig_id, format=None):
        try:
            response = requests.get(baseUrl+'product/'+str(tig_id)+'/')
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
    def get(self, request, tig_id, format=None):
        try:
            response = requests.get(baseUrl+'shipPoint/'+str(tig_id)+'/')
            jsondata = response.json()
            return Response(jsondata)
        except:
            raise Http404
@permission_classes([IsAuthenticated])
class UpdateProductStock(APIView):
    def patch(self, request, tig_id, format=None):
        # Assurez-vous que les données de la demande sont correctement formatées
        # Exemple : {"availability": false}
        data = request.data

        
        # Récupérez le token d'authentification de la requête entrante
        token = request.META.get('HTTP_AUTHORIZATION')

        # Construisez l'URL pour la requête PATCH en utilisant l'ID du produit
        url = f"{baseUrl}product/{str(tig_id)}/"

        # Récupérez le token d'authentification de la requête entrante
        token = request.META.get('HTTP_AUTHORIZATION')
        print(f"Token: {token}")  # Imprimez le token pour vérifier s'il est correctement extrait

         # Ajoutez le token aux headers
        headers = {'Authorization': token}
        # Effectuez la requête PATCH avec les en-têtes d'authentification
        response = requests.patch(url, json=data, headers=headers)

        # Si la mise à jour a réussi, renvoyez les données mises à jour
        if response.status_code == status.HTTP_200_OK:
            jsondata = response.json()
            return Response(jsondata)

        # Sinon, renvoyez une réponse d'erreur
        return Response(response.json(), status=response.status_code)

class UpdateProductSalePercentage(APIView):
    def put(self, request, tig_id, format=None):
        try:
            product_data = request.data
            sale_percentage = product_data.get('sale_percentage')

            if sale_percentage is not None:
                # Récupérez les données du produit à partir de l'API externe
                response = requests.get(baseUrl + f'product/{tig_id}/')
                product = response.json()

                # Mettez à jour le prix en promotion en fonction du pourcentage de promotion
                if 0 <= float(sale_percentage) <= 100:
                    new_price_on_sale = product['price'] * (1 - float(sale_percentage) / 100)
                    product_data['price_on_sale'] = new_price_on_sale
                else:
                    return Response({'error': 'Invalid sale percentage'}, status=status.HTTP_400_BAD_REQUEST)

            # Mettez à jour les données du produit
            response = requests.put(baseUrl + f'product/{tig_id}/', json=product_data)
            jsondata = response.json()
            return Response(jsondata, status=status.HTTP_200_OK)
        except:
            raise Http404
class ProductsByCategory(APIView):

    def get(self, request, category, format=None):
        if category not in ["0", "1", "2"]:
            return Response({"error": "Invalid category"}, status=status.HTTP_400_BAD_REQUEST)

        products = InfoProduct.objects.filter(category=category)
        serializer = InfoProductSerializer(products, many=True)
        return Response(serializer.data)
class UpdateMultipleProductStocks(APIView):
    def put(self, request, format=None):
        products_data = request.data

        for product_data in products_data:
            product_id = product_data.get('id')
            change = product_data.get('change')

            if product_id is None or change is None:
                return Response({"error": "Invalid product data"}, status=HTTP_400_BAD_REQUEST)

            try:
                product = InfoProduct.objects.get(tig_id=product_id)
                new_stock = product.stock + int(change)

                if new_stock >= 0:
                    product.stock = new_stock
                    product.save()
                else:
                    return Response({'error': f'Invalid stock change for product {product_id}'}, status=HTTP_400_BAD_REQUEST)

            except InfoProduct.DoesNotExist:
                return Response({"error": f"Product {product_id} not found"}, status=HTTP_400_BAD_REQUEST)

        return Response({"status": "Stocks updated successfully"}, status=HTTP_200_OK)

class UpdateMultipleProductPromotions(APIView):

    def put(self, request, format=None):
        products_data = request.data

        for product_data in products_data:
            product_id = product_data.get('id')
            sale_percentage = product_data.get('sale_percentage')

            if product_id is None or sale_percentage is None:
                return Response({"error": "Invalid product data"}, status=HTTP_400_BAD_REQUEST)

            try:
                product = InfoProduct.objects.get(tig_id=product_id)

                if 0 <= float(sale_percentage) <= 100:
                    product.sale_percentage = float(sale_percentage)
                    product.price_on_sale = product.price * (1 - float(sale_percentage) / 100)
                    product.save()
                else:
                    return Response({'error': f'Invalid sale percentage for product {product_id}'}, status=HTTP_400_BAD_REQUEST)

            except InfoProduct.DoesNotExist:
                return Response({"error": f"Product {product_id} not found"}, status=HTTP_400_BAD_REQUEST)

        return Response({"status": "Promotions updated successfully"}, status=HTTP_200_OK)


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
    def get_object(self, tig_id):
        try:
            return ProduitEnPromotion.objects.get(tig_id=tig_id)
        except ProduitEnPromotion.DoesNotExist:
            raise Http404

    def get(self, request, tig_id, format=None):
        prod = self.get_object(tig_id)
        serializer = ProduitEnPromotionSerializer(prod)
        response = requests.get(baseUrl+'product/'+str(serializer.data['tigID'])+'/')
        jsondata = response.json()
        return Response(jsondata)
#    def put(self, request, tig_id, format=None):
#        NO DEFITION of put --> server will return "405 NOT ALLOWED"
#    def delete(self, request, tig_id, format=None):
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

