from django import template
from ..models import Question, Tag
from django.urls import reverse
from django.utils.html import format_html_join, format_html


register = template.Library()

@register.simple_tag(takes_context=True)
def tagcloud(context):
    url = reverse('questions:index')
    tags = Tag.objects.order_by('name')
    fmt = '<a href={0}tag/{1}>{2}</a>'
    return format_html_join(', ', fmt, [(url, t.pk, t.name) for t in tags])