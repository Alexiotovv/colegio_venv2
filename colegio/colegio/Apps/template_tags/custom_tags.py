from django import template

register = template.Library()
    
@register.simple_tag
def my_tag():
    return "Hello World from my_tag() custom template tag."

# def almacena(num):
#     val=val+num