from django.urls import path
from mytig import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)

urlpatterns = [
    path('products/', views.RedirectionListeDeProduits.as_view()),
    path('product/<int:pk>/', views.RedirectionDetailProduit.as_view()),
    path('onsaleproducts/', views.PromoList.as_view()),
    path('onsaleproduct/<int:pk>/', views.PromoDetail.as_view()),
    path('shipPoints/', views.RedirectionShipPoints.as_view()),
    path('shipPoint/<int:pk>', views.RedirectionShipPointDetails.as_view()),
    path('availableproducts/', views.AvailableList.as_view()),
    path('availableproduct/<int:pk>/', views.AvailableDetail.as_view()),
    path('infoproducts/', views.InfoProductList.as_view()),
    path('infoproduct/<int:tig_id>/', views.InfoProductDetail.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('update_stock/<int:pk>/', views.UpdateProductStock.as_view(), name='update_product_stock'),
    path('update_sale_percentage/<int:pk>/', views.UpdateProductSalePercentage.as_view(), name='update_product_sale_percentage'),
    path('products_by_category/<str:category>/', views.ProductsByCategory.as_view(), name='products_by_category'),
    path('update_multiple_product_stocks/', views.UpdateMultipleProductStocks.as_view(), name='update_multiple_product_stocks'),
    path('update_multiple_product_promotions/', views.UpdateMultipleProductPromotions.as_view(), name='update_multiple_product_promotions'),

]
