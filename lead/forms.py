from django import forms

from .models import Lead, Comment, LeadFile


from client.models import Client  # Import Client model

class AddLeadForm(forms.ModelForm):
    client = forms.ModelChoiceField(
        queryset=Client.objects.all(),  # Dropdown values
        empty_label="Select a Client",
        required=False  # Optional selection
    )

    class Meta:
        model = Lead
        fields = ('client', 'email', 'description', 'priority', 'status',)  # Changed 'clients' to 'client'





class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)

class AddFileForm(forms.ModelForm):
    class Meta:
        model = LeadFile
        fields = ('file',)