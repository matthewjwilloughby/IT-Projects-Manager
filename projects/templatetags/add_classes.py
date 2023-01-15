from django import template 

register = template.Library()

@register.filter(name="projectRowTitlePriorityClass")
def add_classes(value):
    if value == '1':
        return 'priorityOneAlignLeft'
    elif value == '2':
        return 'priorityTwoAlignLeft'
    else:
       return 'priorityThreeAlignLeft' 
   
   
@register.filter(name="projectRowPriorityClass")
def add_classes(value):
    if value == '1':
        return 'priorityOne'
    elif value == '2':
        return 'priorityTwo'
    else:
       return 'priorityThree' 