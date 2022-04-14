from django import forms
from .models import SubmitAttendance

class SubmitAttendanceForm(forms.ModelForm):

    class Meta:
        model = SubmitAttendance
        fields = ('place', 'in_out')