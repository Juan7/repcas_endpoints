from decimal import Decimal

from rest_framework import serializers


class ClientSerializer(serializers.Serializer):
    
    code = serializers.CharField(max_length=254)
    name = serializers.CharField(max_length=254)
    address = serializers.CharField(max_length=254)
    distributionchannelcode = serializers.CharField(max_length=254)

    
class DistributionChannelSerializer(serializers.Serializer):
    
    code = serializers.CharField(max_length=254)
    description = serializers.CharField(max_length=254)
    

class BillingDocumentSerializer(serializers.Serializer):
    
    code = serializers.CharField(max_length=254)
    documentnumber = serializers.CharField(max_length=254)
    documenttype = serializers.CharField(max_length=254)
    amountpaid = serializers.DecimalField(max_digits=10, decimal_places=4, min_value=Decimal('0.00'))
    totalamount = serializers.DecimalField(max_digits=10, decimal_places=4, min_value=Decimal('0.00'))
    duedate = serializers.DateTimeField()
    registerdate = serializers.DateTimeField()
    uniquecode = serializers.CharField(max_length=254)
    clientcode = serializers.CharField(max_length=254)
    
    
class LaboratorySerializer(serializers.Serializer):
    
    code = serializers.CharField(max_length=254)
    description = serializers.CharField(max_length=254)
    financialdiscountpercentage = serializers.DecimalField(max_digits=10, decimal_places=4, min_value=Decimal('0.00'))
    
    
class ArticleSerializer(serializers.Serializer):
    
    code = serializers.CharField(max_length=254)
    description = serializers.CharField(max_length=254)
    stock = serializers.IntegerField(min_value=0)
    unittype = serializers.CharField(max_length=254)
    laboratorycode = serializers.CharField(max_length=254)
    flagenable = serializers.BooleanField()
    
    
class DistributionChannelPriceSerializer(serializers.Serializer):
    
    articlecode = serializers.CharField(max_length=254)
    distributionchannelcode = serializers.CharField(max_length=254)
    price = serializers.DecimalField(max_digits=10, decimal_places=4, min_value=Decimal('0.00'))


class PromotionSerializer(serializers.Serializer):
    
    articlepromotionablecode = serializers.CharField(max_length=254)
    quantitypromotionable = serializers.IntegerField(min_value=0)
    articlepromotioncode = serializers.CharField(max_length=254)
    quantitypromotion = serializers.IntegerField(min_value=0)
    flagenable = serializers.BooleanField()
    startdate = serializers.DateTimeField()
    enddate = serializers.DateTimeField()


class ScalePriceSerializer(serializers.Serializer):
    
    articlecode = serializers.CharField(max_length=254)
    distributionchannelcode = serializers.CharField(max_length=254)
    startrange = serializers.IntegerField(min_value=0)
    endrange = serializers.IntegerField(min_value=0)
    startdate = serializers.DateTimeField()
    enddate = serializers.DateTimeField()
    scalediscountpercentage = serializers.DecimalField(max_digits=10, decimal_places=4, min_value=Decimal('0.00'))
    

class SpecialPriceSerializer(serializers.Serializer):
    
    clientcode = serializers.CharField(max_length=254)
    articlecode = serializers.CharField(max_length=254)
    startdate = serializers.DateTimeField()
    enddate = serializers.DateTimeField()
    specialdiscountpercentage = serializers.DecimalField(max_digits=10, decimal_places=4, min_value=Decimal('0.00'))
    
    
class SpecialFinantialDiscountSerializer(serializers.Serializer):
    
    clientcode = serializers.CharField(max_length=254)
    laboratorycode = serializers.CharField(max_length=254)
    discountpercentage = serializers.DecimalField(max_digits=10, decimal_places=4, min_value=Decimal('0.00'))

