import django_filters
from .models import *

class RankingFilter(django_filters.FilterSet):

    class Meta:
        model = AthleteRanking
        # fields = '__all__'
        fields = ['Speciality', 'Season', 'AgeGroup']

class PBFilter(django_filters.FilterSet):

    class Meta:
        model = AthletePB
        fields = ['Speciality', 'Season', 'AgeGroup', 'Gender']
