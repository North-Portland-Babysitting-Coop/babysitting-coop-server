from django import forms
from django.forms.utils import ErrorList

class BootstrapErrors(ErrorList):
    def __str__(self):
        return self.as_divs()

    def as_divs(self):
        if not self: return ''
        return '<div class="is-invalid">%s</div>' % ''.join(['<div>%s</div>' % e for e in self])

def add_form_control(attrs={}):
    if attrs is None:
        attrs = {}
    if not "class" in attrs:
        attrs["class"] = "form-control"
    else:
        attrs["class"].split(" ").push("form-control").join(" ")
    return attrs

class TextInput(forms.TextInput):
    def __init__(self, attrs=None):
        super().__init__(add_form_control(attrs))

class PasswordInput(forms.PasswordInput):
    def __init__(self, attrs=None):
        super().__init__(add_form_control(attrs))

class Select(forms.Select):
    def __init__(self, attrs=None):
        super().__init__(add_form_control(attrs))
