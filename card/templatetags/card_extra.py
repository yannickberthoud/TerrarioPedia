from django import template
from card.models import Card

register = template.Library()

@register.inclusion_tag('card/genusoptions.html')
def get_genus_options():
    genus = Card.objects.values('genus').distinct().order_by('genus')
    return { 'genus': genus}