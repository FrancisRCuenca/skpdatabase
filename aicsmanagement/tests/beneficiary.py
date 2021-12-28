from django.test import TestCase
from aicsmanagement.models import Beneficiary

class BeneficiaryTestCase(TestCase):
    """ tests CRUD operations for Beneficiary model """

    def createBeneficiary(self):
        """ Creates default Beneficiary for testing. """

        self.data = {
        'lname':'Dela Cruz', 
        'fname':'Juan',
        'mname':'',
        'mobilenum':'9999999999',
        'barangay': 'Balulang',
        'city': "Cagayan de Oro",
        'assistance': 'CASH',
        'amount': '1000', 
        }

        return Beneficiary.objects.create(data)

    def testBeneficiary(self):
        beneficiary = createBeneficiary()
        self.assertTrue(isinstance(beneficiary, Beneficiary))