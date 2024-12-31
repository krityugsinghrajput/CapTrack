from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from .models import Item
from rest_framework.decorators import api_view
from .serializers import ProductSerializer


class SearchView(APIView):
    def get(self, request):
        query = request.GET.get("query", "")
        category = request.GET.get("category", "All")

        if not query:
            return Response({"error": "Query parameter is required."}, status=status.HTTP_400_BAD_REQUEST)

        products = Item.objects.filter(name__icontains=query)

        if category != "All":
            products = products.filter(category=category)

        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)