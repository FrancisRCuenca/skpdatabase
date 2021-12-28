from rest_framework import serializers
from aicsmanagement.models import Beneficiary

class BeneficiarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Beneficiary
        fields = ['id', 'lname', 'fname', 'mname', 'mobilenum', 'barangay', 'city', 'assistance', 'amount']