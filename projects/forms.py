from django.forms import ModelForm
from .models import Project, ArchivedProjects

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'priority', 'notes',]

    def __init__(self, *args, **kwargs):
        super(ProjectForm,self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update(
            {'class': 'projectTitleInput', 'autocomplete': 'off'})

        self.fields['priority'].widget.attrs.update(
            {'class': 'projectPriorityInput', 'autocomplete': 'off'})
        
        self.fields['notes'].widget.attrs.update(
            {'class': 'projectNotesInput', 'autocomplete': 'off'})



