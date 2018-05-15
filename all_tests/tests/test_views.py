from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from appointment.views import home_page
# from lists.models import Item, List


class HomePageTest(TestCase):

    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')

        html = response.content.decode("utf-8")
        self.assertTrue(html.strip().startswith("<!DOCTYPE html>"))
        self.assertIn("<title>Amazing Leviona's Barbershop</title>", html)
        self.assertTrue(html.endswith("</html>"))


    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'appointment/home_page.html')


#     def test_only_saves_items_when_necessary(self):
#         self.client.get('/')
#         self.assertEqual(Item.objects.count(), 0)


# class ListViewTest(TestCase):

#     def test_uses_list_template(self):
#         list_ = List.objects.create()
#         response = self.client.get('/lists/{}/'.format(list_.id))
#         self.assertTemplateUsed(response, 'lists/list.html')


#     def test_displays_only_items_for_that_list(self):

#         correct_list = List.objects.create()
#         Item.objects.create(text='itemey 1', list=correct_list)
#         Item.objects.create(text='itemey 2', list=correct_list)


#         other_list = List.objects.create()
#         Item.objects.create(text='other list item 1', list=other_list)
#         Item.objects.create(text='other list item 2', list=other_list)


#         response = self.client.get('/lists/{}/'.format(correct_list.id))

#         self.assertContains(response, 'itemey 1')
#         self.assertContains(response, 'itemey 2')
#         self.assertNotContains(response, 'other list item 1')
#         self.assertNotContains(response, 'other list item 2')


#     def test_passes_correct_list_to_template(self):
#         other_list = List.objects.create()
#         correct_list = List.objects.create()
#         response = self.client.get('/lists/{}/'.format(correct_list.id))

#         self.assertEqual(response.context['list'], correct_list)

# class NewListTest(TestCase):
#     def test_can_save_a_POST_request(self):
#         other_list = List.objects.create()
#         correct_list = List.objects.create()


#         # Code Smell: Post Test is too long?
#         response = self.client.post(
#             '/lists/{}/add_item'.format(correct_list.id), 
#             data={'item_text': 'A new item for an existing list'})
#         self.assertEqual(Item.objects.count(), 1)
#         new_item = Item.objects.first()
#         self.assertEqual(new_item.text, 'A new item for an existing list')

#     def test_redirects_after_POST(self):
#         other_list = List.objects.create()
#         correct_list = List.objects.create()
#         response = self.client.post(
#             '/lists/{}/add_item'.format(correct_list.id), 
#             data={
#                 'item_text': 'A new item for an existing list'
#         })
#         self.assertRedirects(response, '/lists/{}/'.format(correct_list.id))



