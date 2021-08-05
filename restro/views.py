from django.shortcuts import render
from rest_framework import permissions
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.decorators import api_view, permission_classes
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication

from .models import Customer, Punjabi, Gujarati, South_Indian, Italian
from .serializers import CustomerSerialize, PunjabiSerialize, GujaratiSerialize, South_IndianSerialize, ItalianSerialize

# Create your views here.
@api_view(['GET'])
@permission_classes([AllowAny])
def api(request):
    api_urls = {
        'Router' : "http://127.0.0.1:8000/router/"
    }
    return Response(api_urls)

# ---------------------------------------------- Model Views ---------------------------------------------------------------------------------

class CustomerView(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerialize
    permission_classes = [IsAuthenticated]
    # authentication_classes = [TokenAuthentication]

# class MenuView(viewsets.ModelViewSet):
#     queryset = Menu.objects.all()
#     serializer_class = MenuSerialize
#     permission_classes = [AllowAny]

# class BillingView(viewsets.ModelViewSet):
#     queryset = Billing.objects.all()
#     serializer_class = BillingSerialize
#     permission_classes = [AllowAny]

class PunjabiView(viewsets.ModelViewSet):
    queryset = Punjabi.objects.all()
    serializer_class = PunjabiSerialize
    permission_classes = [IsAuthenticatedOrReadOnly]

class GujaratiView(viewsets.ModelViewSet):
    queryset = Gujarati.objects.all()
    serializer_class = GujaratiSerialize
    permission_classes = [IsAuthenticatedOrReadOnly]

class South_IndianView(viewsets.ModelViewSet):
    queryset = South_Indian.objects.all()
    serializer_class = South_IndianSerialize
    permission_classes = [IsAuthenticatedOrReadOnly]

class ItalianView(viewsets.ModelViewSet):
    queryset = Italian.objects.all()
    serializer_class = ItalianSerialize
    permission_classes = [IsAuthenticatedOrReadOnly]