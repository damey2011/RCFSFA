from django import forms

from programs.models import Programme


class DateInput(forms.DateInput):
    input_type = 'date'


class ProgrammeForm(forms.ModelForm):
    invited_guests = forms.CharField(widget=forms.Textarea, label="Invited Guests, (seperate with comma)")

    class Meta:
        model = Programme
        fields = '__all__'
        widgets = {
            'start': DateInput(),
            'end': DateInput(),
        }
