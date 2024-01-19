from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.shopItems.as_view(), name='index'),
    path('create',views.shopCreate.as_view(), name='shopCreate'),
    path('<int:pk>', views.ShopDetailView.as_view(), name = 'shop_item'),
    path('<int:pk>', views.CommentCreate.as_view(), name = 'shop_item'),
    path('update/<int:pk>', views.shopitemupdate.as_view(), name = 'shop_item_update'),
    path('delete/<int:pk>', views.ShopItemDelete.as_view(), name = 'shop_item_delete'),
    path('order/<int:pk>', views.OrderDetail.as_view(), name = 'order'),
    path('comment/delete/<int:pk>', views.CommentDelete.as_view(), name = 'comment_delete'),
    path('products/export/', views.ProductDataExportView.as_view(), name = 'product_export')
]