from django import forms
import firebase_admin
from firebase_admin import App,auth
from firebase_admin import credentials
from django.conf import settings
import os
from django.contrib.auth.models import User

from django import forms
from froala_editor.widgets import FroalaEditor

from . import models
cred = credentials.Certificate(os.path.join(settings.BASE_DIR,"google-services.json"))
firebase_admin.initialize_app(cred)


class FirebaseTokenForm(forms.Form):
    token = forms.CharField(required=True)

    def clean_token(self):
        try:
            self.user = auth.get_user(self.cleaned_data['token'])
        except auth.AuthError:
            self.add_error("token","UID is not valid")
            # raise forms.ValidationError("UID is not valid")


    def save(self):
        token = self.cleaned_data['token']

        user,is_new = User.objects.get_or_create(username=self.user.uid,first_name=self.user.display_name)

        if is_new:
            models.FirebaseToken.objects.create(user = user,token=self.user.uid)

        return {
            "is_valid":True,
        }




class HealthTipFrom(forms.ModelForm):
    title = forms.CharField()
    content = forms.CharField(widget=FroalaEditor)

