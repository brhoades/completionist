from django.forms import ModelForm
from checklist.models import Checklist

class ChecklistForm(ModelForm):
    class Meta:
        model = Checklist