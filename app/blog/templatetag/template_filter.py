from django import template

register = template.Library()


@register.filter
def contador_para_listar_imagens(elements, index):
    return elements[index]
