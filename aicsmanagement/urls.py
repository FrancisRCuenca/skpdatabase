from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from aicsmanagement import views

urlpatterns = [
    path('api/beneficiaries/', views.BeneficiaryList.as_view()),
    path('api/beneficiaries/<int:pk>/', views.BeneficiaryDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)