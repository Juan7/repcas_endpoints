from django.db import connection
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from . import serializers 


def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0].lower() for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


class SalesmanViewSet(viewsets.ViewSet):
    
    def get_queryset(self):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM Salesman")
            queryset = dictfetchall(cursor)
        return queryset
    
    def list(self, request):
        serializer = serializers.SalesmanSerializer(self.get_queryset(), many=True)
        return Response(serializer.data)


class ClientViewSet(viewsets.ViewSet):
    
    def get_queryset(self):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM Client")
            queryset = dictfetchall(cursor)
        return queryset
    
    def list(self, request):
        serializer = serializers.ClientSerializer(self.get_queryset(), many=True)
        return Response(serializer.data)
    

class DistributionChannelViewSet(viewsets.ViewSet):
    
    def get_queryset(self):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM DistributionChannel")
            queryset = dictfetchall(cursor)
        return queryset
    
    def list(self, request):
        serializer = serializers.DistributionChannelSerializer(self.get_queryset(), many=True)
        return Response(serializer.data)


class BillingDocumentViewSet(viewsets.ViewSet):
    
    def get_queryset(self):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM BillingDocument")
            queryset = dictfetchall(cursor)
        return queryset
    
    def list(self, request):
        serializer = serializers.BillingDocumentSerializer(self.get_queryset(), many=True)
        return Response(serializer.data)
    

class LaboratoryViewSet(viewsets.ViewSet):
    
    def get_queryset(self):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM Laboratory")
            queryset = dictfetchall(cursor)
        return queryset
    
    def list(self, request):
        serializer = serializers.LaboratorySerializer(self.get_queryset(), many=True)
        return Response(serializer.data)
    
    
class ArticleViewSet(viewsets.ViewSet):
    
    def get_queryset(self):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM Article")
            queryset = dictfetchall(cursor)
        return queryset
    
    def list(self, request):
        serializer = serializers.ArticleSerializer(self.get_queryset(), many=True)
        return Response(serializer.data)    
    
    
class DistributionChannelPriceViewSet(viewsets.ViewSet):
    
    def get_queryset(self):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM Price_DistributionChannel")
            queryset = dictfetchall(cursor)
        return queryset
    
    def list(self, request):
        serializer = serializers.DistributionChannelPriceSerializer(self.get_queryset(), many=True)
        return Response(serializer.data)    
    
    
class PromotionViewSet(viewsets.ViewSet):
    
    def get_queryset(self):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM Promotion")
            queryset = dictfetchall(cursor)
        return queryset
    
    def list(self, request):
        serializer = serializers.PromotionSerializer(self.get_queryset(), many=True)
        return Response(serializer.data) 
    

class ScalePriceViewSet(viewsets.ViewSet):
    
    def get_queryset(self):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM ScalesPrice")
            queryset = dictfetchall(cursor)
        return queryset
    
    def list(self, request):
        serializer = serializers.ScalePriceSerializer(self.get_queryset(), many=True)
        return Response(serializer.data) 


class SpecialPriceViewSet(viewsets.ViewSet):
    
    def get_queryset(self):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM SpecialPrice")
            queryset = dictfetchall(cursor)
        return queryset
    
    def list(self, request):
        serializer = serializers.SpecialPriceSerializer(self.get_queryset(), many=True)
        return Response(serializer.data) 
    
    
class SpecialFinantialDiscountViewSet(viewsets.ViewSet):
    
    def get_queryset(self):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM SpecialFinancialDsct")
            queryset = dictfetchall(cursor)
        return queryset
    
    def list(self, request):
        serializer = serializers.SpecialFinantialDiscountSerializer(self.get_queryset(), many=True)
        return Response(serializer.data) 
