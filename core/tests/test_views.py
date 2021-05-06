from django.urls import reverse,resolve
from django.test import TestCase
from .. views import home,board_topics,new_topic
from ..models import Board,Topic,Post
from django.contrib.auth.models import User
from ..forms import NewTopicForm

# Create your tests here.
'''
class HomeTests(TestCase):
    def setUp(self):
        self.board = Board.objects.create(name='Django',description='Django board.')
        url = reverse('home')
        self.reponse = self.client.get(url)

    def test_home_view_status_code(self):
        self.assertEquals(self.reponse.status_code,200)

 
    def test_home_view_status_code(self):

        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code,200)
        
          

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func,home)
    
    def test_home_view_contains_link_to_topics_page(self):
        board_topics_url = reverse('board_topics',kwargs={'pk':self.board.pk})
        self.assertContains(self.reponse, 'href="{0}"'.format(board_topics_url))

    def test_board_toics_view_contains_link_back_to_homepage(self):
        board_topics_url = reverse('board_topics',kwargs={'pk':1})
        response = self.client.get(board_topics_url)
        homepage_url = reverse('home')
        self.assertContains(response,'href="{0}"'.format(homepage_url))
      

class BoardTopicsTests(TestCase):
    def setUp(self):
        Board.objects.create(name='Django', description='Django Board.')
    
    def test_board_topics_view_seccess_status_code(self):
        url = reverse('board_topics', kwargs={'pk':1})
        response = self.client.get(url)
        self.assertEquals(response.status_code,200)
    
    def test_board_topics_view_not_found_status_code(self):
        url = reverse('board_topics',kwargs={'pk':33})
        reponse = self.client.get(url)
        self.assertEquals(reponse.status_code,404)
    
    def test_board_topics_url_resolves_board_topics_view(self):
        view=resolve('/boards/1/')
        self.assertEquals(view.func,board_topics) 
        '''
# new topic test
'''
class NewtopicTests(TestCase):
    def setUp(self):
        Board.objects.create(name='Django',description='Django Board.')
    
    def test_new_topic_view_success_status_code(self):
        url = reverse('new_topic',kwargs={'pk':1})
        response = self.client.get(url)
        self.assertEquals(response.status_code,200)
    
    def test_new_topic_view_not_found_status_code(self):
        url = reverse('new_topic',kwargs={'pk':33})
        response = self.client.get(url)
        self.assertEquals(response.status_code,404)
    
    def test_new_topic_url_resolves_new_topic_view(self):
        view = resolve('/boards/1/new/')
        self.assertEquals(view.func,new_topic)

    def test_new_topic_view_contains_link_back_to_board_topics_view(self):
        new_topic_url = reverse('new_topic',kwargs={'pk':1})
        board_topics_url =reverse('board_topics', kwargs={'pk':1})
        response = self.client.get(new_topic_url)
        self.assertContains(response,'href="{0}"'.format(board_topics_url))

    def test_board_topics_view_contains_navigation_links(self):
        board_topics_url = reverse('board_topics', kwargs ={'pk':1})
        homepage_url = reverse('home')
        new_topic_url = reverse('new_topic',kwargs={'pk':1})
        response = self.client.get(board_topics_url)
        self.assertContains(response,'href="{0}"'.format(homepage_url))
        self.assertContains(response,'href="{0}"'.format(new_topic_url))

        '''

    # new topic test with post 
'''
class NewtopicTests2(TestCase):
    def setUp(self):
        Board.objects.create(name='Django', description='Django board.')
        User.objects.create_user(username='john', email='john@doe.com', password='123')

    def test_csrf(self):
        url = reverse('new_topic',kwargs = {'pk':1})
        response = self.client.get(url)
        self.assertContains(response,'csrfmiddlewaretoken')

    def test_new_topic_valid_post_data(self):
        url = reverse('new_topic', kwargs={'pk':1})
        data = {
            'subject': 'Testing subject',
            'message': 'This is testing message from testcase'

        }
        response = self.client.get(url,data)
        #self.assertTrue(Topic.objects.exists()) #here is one problem
        #self.assertTrue(Post.objects.exists())

    def test_new_topic_invalid_post_data(self):
        url = reverse('new_topic',kwargs={'pk':1})
        response = self.client.get(url,{})
        self.assertEquals(response.status_code,200)
    
    def test_new_topicinvalid_post_data_empty_fields(self):
        url = reverse('new_topic',kwargs={'pk':1})
        data = {
            'subject':'',
            'message':''
        }
        response = self.client.get(url,data)
        self.assertEquals(response.status_code,200)
        self.assertFalse(Topic.objects.exists())
        self.assertFalse(Post.objects.exists())
    
    def test_contains_form(self):
        url = reverse('new_topic',kwargs={'pk':1})
        response = self.client.get(url)
        form = response.context.get('form')
        self.assertInsInstance(form,NewTopicForm)

    def test_new_topic_invalid_post_data(self):
        url = reverse('new_topic',kwargs={'pk':1})
        response = self.client.get(url,{})
        form = response.context.get('form')
        self.assertEquals(response.status_code, 200)
        self.assertTrue(form.errors)

    '''