from django.forms import ModelForm, TextInput
from datetime import datetime, date
from .models import Record

class RecordForm(ModelForm):
	class Meta:
		model = Record
		fields = ['date','description','category','cash','balance_type']
		widgets = {
			'date':TextInput(
				attrs={
					'id':'datepicker1',
					'value':date.today().strftime("%Y-%m-%d")
				}
				)
		}
