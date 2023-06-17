from django.urls import path
# from django.conf import settings
# from django.conf.urls.static import static
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import (
    ProductListView,
    ProductDetailView,
    OrderView,
    ThankYouView,
)

app_name = "product"
urlpatterns = [
    path("", ProductListView.as_view(), name="product-list"),
    path("<int:pk>/detail/", ProductDetailView.as_view(), name="product-detail"),
    path("<int:pk>/detail/order/", OrderView.as_view(), name="product-order"),
    path("<int:pk>/detail/order/thank-you/", ThankYouView.as_view(), name="thank-you"),
] 
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# urlpatterns += staticfiles_urlpatterns()
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)