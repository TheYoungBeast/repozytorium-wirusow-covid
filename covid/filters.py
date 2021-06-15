import django_filters
from django.db import models
from covid.models import Genome

class GenomeFilter(django_filters.FilterSet):
    CollectionDate = django_filters.DateFromToRangeFilter()
    class Meta:
        model = Genome
        fields = ['Accession', 'Host', 'Country',]
        filter_overrides = {
            models.CharField: {
                'filter_class': django_filters.CharFilter,
                'extra': lambda f: {
                    'lookup_expr': 'icontains',
                },
            }
        }