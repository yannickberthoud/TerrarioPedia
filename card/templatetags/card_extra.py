from django import template
from card.models import Category

register = template.Library()

@register.inclusion_tag('card/links.html')
def get_nav_category():
    categories = Category.objects.order_by('name')
    return {'categories': categories}