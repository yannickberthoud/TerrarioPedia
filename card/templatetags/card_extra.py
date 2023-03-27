from django import template
from card.models import Category, Card

register = template.Library()

@register.inclusion_tag('card/links.html')
def get_nav_category():
    categories = Category.objects.order_by('name')
    return {'categories': categories}

@register.inclusion_tag('card/genusoptions.html')
def get_genus_options():
    genus = Card.objects.values('genus').distinct()
    return { 'genus': genus}