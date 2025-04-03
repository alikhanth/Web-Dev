from django.urls import path
from .views import *

urlpatterns = [
    # Company Endpoints
    path('companies/', CompanyListCreateView.as_view(), name='company-list'),
    path('companies/<int:pk>/', CompanyDetailView.as_view(), name='company-detail'),
    path('companies/<int:id>/vacancies/', VacancyByCompanyView.as_view(), name='vacancies-by-company'),

    # Vacancy Endpoints
    path('vacancies/', VacancyListCreateView.as_view(), name='vacancy-list'),
    path('vacancies/<int:id>/', VacancyDetailView.as_view(), name='vacancy-detail'),
    path('vacancies/top_ten/', TopTenVacanciesView.as_view(), name='top-ten-vacancies'),
]
