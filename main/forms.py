from django import forms
from main.models import DirectMessage,GroupMessage
from phonenumber_field.formfields import PhoneNumberField
from django.core.exceptions import ValidationError


interval_choice=(
    ('every hour', 'Every Hour'),
    ('everyday', 'Everyday'),
    ('every week', 'Every Week')
)

class MessageForm(forms.ModelForm):
    intervals=forms.ChoiceField(choices=interval_choice, required=False, widget=forms.Select(attrs={'class':'form-select','id':'floatingSelect',}),)
    # wait_time=forms.IntegerField(required=False)
    class Meta:
        fields = "__all__"
        widgets = { 
            'phone_no' : forms.NumberInput(attrs={'class':'form-control','id':'typePhone','placeholder':'phone_no','type':'tel'}),
            'group_id' : forms.TextInput(attrs={'class':'form-control','id':'floatingInput','placeholder':'group_id','type':'text'}),
            'message': forms.Textarea(attrs={'class':'form-control','id':'floatingTextarea','placeholder':'message','type':'text','cols':'', 'rows':''}),
            'time': forms.TimeInput(attrs={'class':'form-control','id':'floatingInput time','type':'time',}),
            'date': forms.DateInput(attrs={'class':'form-control','id':'floatingInput date','type':'date',}),
            'interval':forms.NumberInput(attrs={'class':'form-control','id':'floatingInput number','type':'number'}),
            'interval_period': forms.Select(attrs={'class':'form-select','id':'floatingSelect',}),
            # 'intervals': forms.Select(attrs={'class':'form-select','id':'floatingSelect',}),
            'status': forms.Select(attrs={'class':'form-select','id':'floatingSelect',}),
            'tab_close': forms.Select(attrs={'class':'form-select','id':'floatingSelect',}),
            'close_time':forms.NumberInput(attrs={'class':'form-control','id':'floatingInput number','type':'number'}),

            'wait_time':forms.NumberInput(attrs={'class':'form-control','id':'floatingInput number','type':'number'}),
            'one_off': forms.Select(attrs={'class':'form-select','id':'floatingSelect',}),
                }

    # def clean_data(self):
    #     return 

    def clean(self):
        cleaned_data = self.cleaned_data
        intervals=cleaned_data.get('intervals')
        tab_close=cleaned_data.get('tab_close')
        close_time =cleaned_data.get('close_time')
        if close_time is not None:
            if tab_close==False and close_time > 0:
                raise ValidationError('ensure tab close is true')
        if intervals=='every hour':
            cleaned_data['interval']='1'
            cleaned_data['interval_period']='hours'
        elif intervals=='everyday':
            cleaned_data['interval']='1'
            cleaned_data['interval_period']='days'
        elif intervals=='every week':
            cleaned_data['interval']='7'
            cleaned_data['interval_period']='days'
        
        return cleaned_data

class DirectForm(MessageForm):
    phone_no=PhoneNumberField

    class Meta(MessageForm.Meta):
        model=DirectMessage

    # def clean_data(self):
    #     return super(DirectForm, self).clean()


class GroupForm(MessageForm):
    group_id=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','id':'floatingInput'}))

    class Meta(MessageForm.Meta):
        model=GroupMessage

    # def clean_data(self):
    #     return super(GroupForm, self).clean()
