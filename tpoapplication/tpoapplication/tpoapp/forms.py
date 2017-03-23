from django.forms import ModelForm
from tpoapp.models import Drive

class ViewForm(ModelForm):
    class Meta:
        model = Drive
        fields = '__all__'
