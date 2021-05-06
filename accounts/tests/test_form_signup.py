from django.test import TestCase
from ..forms import SignUpForm


class SignUpFormTest(TestCase):
    def test_form_has_fields(self):
        form =SignUpForm()
        expected = ['username','password1','password2','email']
        actual = list(form.fields)
        self.assertSequenceEqual(expected,actual)