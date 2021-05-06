from django.test import TestCase
from django.contrib.auth.forms import UserCreationForm
from django.urls import resolve,reverse
from ..views import singup
from django.contrib.auth.models import User
from ..forms import SignUpForm
# Create your tests here.

class SingUpTest(TestCase):
    '''
 def test_signup_status_code(self):
    url = reverse('singup')
    response = self.client.get(url)
    self.assertEquals(response.status_code,200)

def test_singup_url_resolves_singup_view(self):
    view = resolve('singup')
    self.assertEquals(view.func,singup) '''
'''
def setUp(self):
    url = reverse('signup')
    self.response = self.client.get(url)

def test_singUp_status_code(self):
    self.assertEquals(self.response.status_code,200)

def test_singup_url_resolve_singup_view(self):
    view = resolve('/signup/')
    self.asserEquals(view.func,singup)

def test_csrf(self):
    self.assertContains(self.response,'csrfmiddlewaretoken')

def test_contains_form(self):
    form = self.response.context.get('form')
    self.assertIsInstance(form,SignUpForm)
def test_form_inputs(self):
        
        self.assertContains(self.response, '<input', 5)
        self.assertContains(self.response, 'type="text"', 1)
        self.assertContains(self.response, 'type="email"', 1)
        self.assertContains(self.response, 'type="password"', 2)

class SuccesfulSingUpTests(TestCase):
    def setUp(self):
        url = reverse("singup")
        data = {
            'username':'john',
            'password1':'1234adcd',
            'password2':'1234adcd'
        }
        self.response = self.client.post(url,data)
        self.home_url = reverse('home')
    
    def test_redirection(self):
        self.assertRedirects(self.response,self.home_url)

    def test_user_creation(self):
        self.assertTrue(User.objects.exists())
    
    def test_user_authontiction(self):
        response = self.client.get(self.home_url)
        user = response.context.get('user')
        self.assertTrue(user.is_authenticated)

class SuccessfulSignUpTests(TestCase):
   def setUp(self):
        url = reverse('signup')
        data = {
            'username': 'john',
            'password1': 'abcdef123456',
            'password2': 'abcdef123456'
        }
        self.response = self.client.post(url, data)
        self.home_url = reverse('home')

   def test_redirection(self):
      
        self.assertRedirects(self.response, self.home_url)

   def test_user_creation(self):
        self.assertTrue(User.objects.exists())

   def test_user_authentication(self):
      
        response = self.client.get(self.home_url)
        user = response.context.get('user')
        self.assertTrue(user.is_authenticated)
        '''