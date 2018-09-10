from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string

from lists.views import home_page
from lists.models import Item

class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)
        response = self.client.get('/')
        
    
    '''
    def test_home_page_returns_correct_html(self):
        print("teste1")
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')

        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.strip().endswith('</html>'))

    def test_home_page_returns_correct_html(self):
        print("teste 2")
        response = self.client.get('/')  

        html = response.content.decode('utf8')  
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.strip().endswith('</html>'))

        self.assertTemplateUsed(response, 'home.html')
    '''
    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')

        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.strip().endswith('</html>'))

        self.assertTemplateUsed(response, 'home.html')

    def test_uses_home_template (self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
    
    def test_can_save_a_POST_request(self):
        
        self.client.post('/', data={'item_text':"A new list item"})
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

        #self.assertEqual(response.status_code,302)
        #self.assertEqual(response['location'], '/')

    def test_redirects_after_POST_request(self):
        response = self.client.post('/', data={'item_text':'A new list item'})
        self.assertEqual(response.status_code , 302)
        self.assertEqual(response['location'], '/')


    def test_display_all_list_items(self):
        Item.objects.create(text='itemey 1')
        Item.objects.create(text='itemey 2')

        response = self.client.get('/')
        self.assertIn('itemey 1', response.content.decode())
        self.assertIn('itemey 2', response.content.decode())
        print(response.content.decode())



'''
    def test_only_save_items_when_necessary(self):
        self.client.get('/')

        self.assertEqual(Item.objects.count(), 0)

'''