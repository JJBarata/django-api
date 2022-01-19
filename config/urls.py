from django.contrib import admin
from django.urls import path, include
from financiall.views import ReceitaViewSet, DespesaViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'receitas', ReceitaViewSet)
router.register(r'despesas', DespesaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
