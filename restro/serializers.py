
from rest_framework import serializers
from .models import Customer, Punjabi, Gujarati, South_Indian, Italian


# class MenuSerialize(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Menu
#         fields = ['id', 'url', 'Dish1', 'Dish2', 'Dish3', 'Dish4', 'Category',]

class PunjabiSerialize(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Punjabi
        fields = ['id', 'url', 'Sabji_Name', 'Price']

class GujaratiSerialize(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Gujarati
        fields = ['id', 'url', 'Sabji_Name', 'Price']

class South_IndianSerialize(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = South_Indian
        fields = ['id', 'url', 'Name', 'Price']

class ItalianSerialize(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Italian
        fields = ['id', 'url', 'Name', 'Price']

# class BillingSerialize(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Billing
#         fields = ['id', 'url', 'Price', 'Fare1',]

class CustomerSerialize(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'url', 'Name', 'Dish1', 'Dish2', 'Dish3', 'Dish4']
                