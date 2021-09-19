import django_filters
from ..models import *

class CategoryFilter(django_filters.FilterSet):
    category = django_filters.ChoiceFilter()

    def __init__(self, data=None, *args, **kwargs):
        super(CategoryFilter, self).__init__(*args, **kwargs)
        # print(self.filters['category'].extra['choices'])
        # self.filters['category'].extra['choices'] = [option.category for option in categories.objects.all()]
        # print(self.filters['category'].extra['choices'])

    class Meta:
        model = categories
        fields = ['user', 'category']