import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from mytig.config import baseUrl
from mytig.models import InfoProduct
from mytig.serializers import InfoProductSerializer
from rest_framework import status
from django.http import Http404, JsonResponse
from rest_framework_simplejwt.tokens import AccessToken
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from mytig.models import ProduitEnPromotion, AvailableProduct
from mytig.serializers import ProduitEnPromotionSerializer, AvailableProductSerializer

class InfoProductList(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        products = InfoProduct.objects.all()
        serializer = InfoProductSerializer(products, many=True)
        return Response(serializer.data)


class InfoProductDetail(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, tig_id, format=None):
        try:
            product = InfoProduct.objects.get(tig_id=tig_id)
            serializer = InfoProductSerializer(product)
            return Response(serializer.data)
        except InfoProduct.DoesNotExist:
            raise Http404

class UpdateProductStock(APIView):
    def patch(self, request, tig_id):
        try:
            product = InfoProduct.objects.get(tig_id=tig_id)
        except InfoProduct.DoesNotExist:
            return Response({"error": f"Product {tig_id} not found"}, status=status.HTTP_404_NOT_FOUND)

        try:
            quantityInStock = request.data["quantityInStock"]
            new_stock = product.quantityInStock + int(quantityInStock)
            if new_stock < 0:
                return Response({"error": "Stock cannot be negative"}, status=status.HTTP_400_BAD_REQUEST)

            product.quantityInStock = new_stock
            product.save()
            serializer = InfoProductSerializer(product)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except KeyError:
            return Response({"error": "Missing parameter 'quantityInStock'"}, status=status.HTTP_400_BAD_REQUEST)

        except ValueError:
            return Response({"error": "Invalid parameter 'quantityInStock'"}, status=status.HTTP_400_BAD_REQUEST)

class UpdateProductSalePercentage(APIView):
    def put(self, request, tig_id, format=None):
        try:
            product_data = request.data
            sale_percentage = product_data.get('discount')

            if sale_percentage is not None:
                # Récupérez le produit de la base de données
                try:
                    product = InfoProduct.objects.get(tig_id=tig_id)
                except InfoProduct.DoesNotExist:
                    return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

                # Mettez à jour les données de promotion du produit
                if 0 <= float(sale_percentage) <= 100:
                    product.sale_percentage = float(sale_percentage)
                    product.price_on_sale = product.price * (1 - float(sale_percentage) / 100)
                    product.sale = True
                    product.save()
                else:
                    return Response({'error': 'Invalid sale percentage'}, status=status.HTTP_400_BAD_REQUEST)

            serializer = InfoProductSerializer(product)
            return Response(serializer.data, status=status.HTTP_200_OK)
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
            '''
            Ce if vérifie si la clé 'id' et la clé 'quantityInStock' sont présentes dans le dictionnaire product_data. Si l'une ou l'autre de ces clés est absente, cela signifie que les données fournies pour la mise à jour du stock sont invalides. Par conséquent, la condition retournera True et la réponse renvoyée sera une erreur 400 Bad Request.

            La fonction all() prend un itérable (ici, un objet dict en tant que dictionnaire de données du produit) et retourne True si tous les éléments sont True, sinon False. Dans ce cas, cela signifie que la condition retournera True si toutes les clés 'id' et 'quantityInStock' sont présentes dans le dictionnaire product_data.
            '''
            if not all(k in product_data for k in ('id', 'quantityInStock')):
                return Response({"error": "Invalid product data"}, status=HTTP_400_BAD_REQUEST)

            product_id = product_data.get('id')
            quantityInStock = product_data.get('quantityInStock')

            if product_id is None or quantityInStock is None:
                return Response({"error": "Invalid product data"}, status=HTTP_400_BAD_REQUEST)

            try:
                product = InfoProduct.objects.get(tig_id=product_id)
                new_stock = product.quantityInStock + int(quantityInStock)

                if new_stock >= 0:
                    product.quantityInStock = new_stock
                    product.save()
                else:
                    return Response({'error': f'Invalid quantityInStock for product {product_id}'}, status=HTTP_400_BAD_REQUEST)

            except InfoProduct.DoesNotExist:
                return Response({"error": f"Product {product_id} not found"}, status=HTTP_400_BAD_REQUEST)

        return Response({"status": "quantityInStock updated successfully"}, status=HTTP_200_OK)


class UpdateMultipleProductPromotions(APIView):

    def put(self, request, format=None):
        products_data = request.data

        for product_data in products_data:
            if not all(k in product_data for k in ('id', 'sale', 'discount')):
                return Response({"error": "Invalid product data"}, status=HTTP_400_BAD_REQUEST)

            product_id = product_data.get('id')
            sale = product_data.get('sale')
            discount = product_data.get('discount')

            if product_id is None or sale is None or discount is None:
                return Response({"error": "Invalid product data"}, status=HTTP_400_BAD_REQUEST)

            try:
                product = InfoProduct.objects.get(tig_id=product_id)

                # Mise à jour du champ "sale" du produit
                product.sale = sale

                # Mise à jour du champ "discount" du produit
                if 0 <= float(discount) <= 100:
                    product.discount = float(discount)
                    product.price_on_sale = product.price * (1 - float(discount) / 100)
                    product.save()
                else:
                    return Response({'error': f'Invalid discount for product {product_id}'}, status=HTTP_400_BAD_REQUEST)

            except InfoProduct.DoesNotExist:
                return Response({"error": f"Product {product_id} not found"}, status=HTTP_400_BAD_REQUEST)

        return Response({"status": "Promotions updated successfully"}, status=HTTP_200_OK)



class PromoList(APIView):
    def get(self, request, format=None):
        res = []
        for prod in ProduitEnPromotion.objects.all():
            serializer = ProduitEnPromotionSerializer(prod)
            try:
                product = InfoProduct.objects.get(tig_id=serializer.data['tigID'])
                res.append(product.to_dict())
            except InfoProduct.DoesNotExist:
                pass
        return JsonResponse(res, safe=False)


class PromoDetail(APIView):
    def get_object(self, tig_id):
        try:
            return ProduitEnPromotion.objects.get(tig_id=tig_id)
        except ProduitEnPromotion.DoesNotExist:
            raise Http404

    def get(self, request, tig_id, format=None):
        prod = self.get_object(tig_id)
        serializer = ProduitEnPromotionSerializer(prod)
        try:
            product = InfoProduct.objects.get(tig_id=serializer.data['tigID'])
            return Response(product.to_dict())
        except InfoProduct.DoesNotExist:
            return Response({"error": f"Product {serializer.data['tigID']} not found"}, status=HTTP_400_BAD_REQUEST)


class AvailableList(APIView):
    def get(self, request, format=None):
        res = []
        for prod in AvailableProduct.objects.all():
            serializer = AvailableProductSerializer(prod)
            try:
                product = InfoProduct.objects.get(tig_id=serializer.data['tigID'])
                res.append(product.to_dict())
            except InfoProduct.DoesNotExist:
                pass
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
        try:
            product = InfoProduct.objects.get(tig_id=serializer.data['tigID'])
            return Response(product.to_dict())
        except InfoProduct.DoesNotExist:
            return Response({"error": f"Product {serializer.data['tigID']} not found"}, status=HTTP_400_BAD_REQUEST)


