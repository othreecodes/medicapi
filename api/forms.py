from django import forms
from firebase_admin import App
from django.conf import settings

# firebaseapp = App(name="AwQAd")

class FirebaseTokenForm(forms.Form):
    token = forms.CharField(required=True)


    def save(self):
        token = self.cleaned_data['token']
        pass
