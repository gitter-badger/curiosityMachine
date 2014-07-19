from django import forms
from django_bleach.forms import BleachField
from django.conf import settings

class MaterialsForm(forms.Form):
    materials = BleachField(required=True,
                        allowed_tags=settings.BLEACH_ALLOWED_TAGS,
                        allowed_attributes=settings.BLEACH_LIB_ATTRIBUTES,
                        allowed_styles=settings.BLEACH_ALLOWED_STYLES)

    def __init__(self, *args, **kwargs):
        progress = kwargs.pop('progress')
        super(MaterialsForm, self).__init__(*args, **kwargs)
        self.fields['materials'].initial = progress.materials_list

class EditComment(forms.Form):
    comments = forms.CharField(required=True)
    #about_research = forms.CharField(required=True, label="About My Research")

    def __init__(self, request, *args, **kwargs):
        comment = kwargs.pop('comment')
        super(EditComment, self).__init__(*args, **kwargs)
        self._request = request
        self.user = request.user
        self.fields['comments'].initial = comment.content