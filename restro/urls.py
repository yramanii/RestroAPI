from django.db import router
from rest_framework import routers, urlpatterns
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register("customer", views.CustomerView)
# router.register("menu", views.MenuView)
# router.register("billing", views.BillingView)
router.register("punjabi", views.PunjabiView)
router.register("gujarati", views.GujaratiView)
router.register("south_indian", views.South_IndianView)
router.register("italian", views.ItalianView)


urlpatterns = [
    path('', views.api, name='api'),
    path('api-auth/', include('rest_framework.urls')),
    path('router/', include(router.urls)),
]