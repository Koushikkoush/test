from django import forms

from .models import Client, Comment, ClientFile

class AddClientForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "w-full py-4 px-6 rounded-xl bg-gray-100", "placeholder": "Company Name"})
    )
    email = forms.CharField(
        widget=forms.TextInput(attrs={"class": "w-full py-4 px-6 rounded-xl bg-gray-100","placeholder": "E-mail"})
    )
    phone_number = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"class": "w-full py-4 px-6 rounded-xl bg-gray-100", "placeholder": "Phone Number"})
    )
    service = forms.ChoiceField(
        choices=Client.SERVICE_CHOICES,
        widget=forms.Select(attrs={"class": "w-full py-4 px-6 rounded-xl bg-gray-100"})
    )
    contacted_person_name = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"class": "w-full py-4 px-6 rounded-xl bg-gray-100", "placeholder": "Contacted person"})
    )
    custom_service = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"class": "w-full py-4 px-6 rounded-xl bg-gray-100", "placeholder": "Other (Specify)"})
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={"rows": "5", "class": "w-full bg-gray-100 rounded-xl","placeholder": "Description"})
    )

    class Meta:
        model = Client
        fields = ('name', 'email', 'phone_number', 'service', 'custom_service', 'description',)

class AddCommentForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(attrs={"rows":"5", "class": "w-full bg-gray-100 rounded-xl"})
    )

    class Meta:
        model = Comment
        fields = ('content',)

class AddFileForm(forms.ModelForm):
    class Meta:
        model = ClientFile
        fields = ('file',)