from django.forms import ModelForm
from .models import AuthUser
class AuthUserForm(ModelForm):
    class Meta:
        model = AuthUser
        fields = "__all__"
    