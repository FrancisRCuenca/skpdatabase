from django.http import Http404

from rest_framework import status
from rest_framework.views import APIView 
from rest_framework.response import Response

from aicsmanagement.models import Beneficiary
from aicsmanagement.serializers import BeneficiarySerializer

class BeneficiaryList(APIView):
    """
    POST method or GET method for all Beneficiaries
    """

    def get(self, request, format=None):
        beneficiaries = Beneficiary.objects.all()
        serializer = BeneficiarySerializer(beneficiaries, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BeneficiarySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BeneficiaryDetail(APIView):
    """
    PUT and DELETE methods, or GET specific Beneficiary
    """

    def get_object(self, pk):
        try:
            return Beneficiary.objects.get(pk=pk)
        except Beneficiary.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        beneficiary = self.get_object(pk)
        serializer = BeneficiarySerializer(beneficiary)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        beneficiary = self.get_object(pk)
        serializer = BeneficiarySerializer(beneficiary, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        beneficiary = self.get_object(pk)
        beneficiary.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)