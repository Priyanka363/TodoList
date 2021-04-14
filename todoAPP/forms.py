from django.forms import ModelForm
from todoAPP.models import List

class add_todo(ModelForm):
  class Meta:
    model=List
    fields=['title','status','precedence']