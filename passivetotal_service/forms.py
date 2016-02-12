from django import forms

class PassiveTotalConfigForm(forms.Form):
    error_css_class = 'error'
    required_css_class = 'required'
    pt_api_key = forms.CharField(required=True,
                                 label="API Key",
                                 widget=forms.TextInput(),
                                 help_text="Obtain API key from PassiveTotal.",
                                 initial='')
    pt_query_url = forms.CharField(required=True,
                                   label="Query URL",
                                   widget=forms.TextInput(),
                                   initial='https://www.passivetotal.org/api/v1')

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', ':')
        super(PassiveTotalConfigForm, self).__init__(*args, **kwargs)
