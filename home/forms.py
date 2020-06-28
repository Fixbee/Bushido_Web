from django.forms import ModelForm
from home.models import NewRegistration


class RegistrationForm(ModelForm):
	class Meta:
		model = NewRegistration
		fields = "__all__"  