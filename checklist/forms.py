from django.forms import ModelForm
from checklist.models import Checklist, Run

class ChecklistForm(ModelForm):
    class Meta:
        model = Checklist

class RunForm(ModelForm):
    class Meta:
        model = Run
        fields = [ 'name', 'description' ] 
