from django.core import mail
from django.contrib.auth.models import User
from django.urls import reverse,resolve
from django.test import TestCase

from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import unsafe_base64_encode 
from django.contrib.auth import views  as auth_views
from django.contrib.auth.forms import SetPasswordForm


class PasswordResetMailTests(TestCase):
    def setUp(self):
        User.objects.create_user(username='john',email='john@doe.com',password='123')
        self.email = mail.outbox[0]

    def test_email_subject(self):
        self.assertEqual('[MNR Blog team] Please reset your passwsord',self.email.subject)
    
    def test_email_body(self):
        context = self.response.context
        token = context.get('token')
        uid = context.get('uid')
        password_reset_token_url = reverse('password_reset_confirm',kwargs={
            'uid64':uid,
            'token':token
        })
        self.assertIn(password_reset_token_url,self.email.body)
        self.assertIn('john',self.email.body)
        self.assertIn('john@doe.com',self.email.body)

    def test_email_to(self):
        self.assertEqual(['john@doe.com',self.email.to])

class PasswordResetDoneTests(TestCase):
    def setUp(self):
        url = reverse('password_reset_done')
        self.response = self.client.get(url)

    def test_status_code(self):
        self.assertEquals(self.response.status_code,200)

    def test_view_fuction(self):
        view = resolve('/reset/done/')
        self.assertEquals(view.func.view_class,auth_views.PasswordResetDoneView)


class PasswordResetConfirmTests(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='john',email ='john@doe.com',password='123')
        self.uid = urlsafe_base63_encode(force_bytes(user.pk)).decode()
        self.token = defualt_token_generator.make_token(user)
        
    def test_status_code(self):
        self.assertEquals(self.response.status_code,200)
    
    def test_view_fuction(self):
        view = resolve('/reset/{uid64}/{token}'.format(uid64=self.uid,token=self.token))
        self.assertEquals(view.func.view_class, auth_views.PasswordResetConfirmView)
    
    def test_csrf(self):
        self.assertContains(self.response,'csrmiddlewaretoken')

    def test_contains_form(self):
        form =self.response.context.get('form')
        self.assertIsInstance(form,SetPasswordForm)
    
    def test_from_inputs(self):
        self.assertContains(self.response,'<input',3)
        self.assertContains(self.response,'type="password"',2)

    
class InvalidPasswordRestConfirmationTests(self):

    def setUp(self):
        user = User.objects.create_user(username='john',email='john@deo.com',password='123')
        uid = urlsafe_base64_encode(force_bytes(user.pk)).decode()
        token = defualt_token_generator.make_token(user)

        user.set_password('abr123')
        user.save()
        url= reverse('password_reset_confirm',kwargs={'uid64':uid,'token':token})
        self.response = self.client.get(url)

    def test_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_html(self):
        password_reset_url = reverse('password_reset')
        self.assertContains(self.response, 'invalid password reset link')
        self.assertContains(self.response, 'href="{0}"'.format(password_reset_url))

class PasswordResetCompleteTests(TestCase):
    def setUp(self):
        url = reverse('password_reset_complete')
        self.response = self.client.get(url)

    def test_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_view_function(self):
        view = resolve('/reset/complete/')
        self.assertEquals(view.func.view_class, auth_views.PasswordResetCompleteView)


    
