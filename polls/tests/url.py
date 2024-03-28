import json
from django.test import TestCase
from polls.serializers import *

# Create your tests here.
class CallIndex(TestCase):
        def test_index(self):
                response = self.client.get("/api/v1/")
                actual = response.content
                expected_content = b"<!DOCTYPE html>\n<html>\n<body>\n\n<h1>Hello World!</h1>\n\n</body>\n</html>"
                self.assertEqual(actual, expected_content)
                self.assertEqual(response.status_code, 200)
        
        def test_get_post(self):
                Post.objects.create(title="Peppa",content="pig",pub_date="1989-10-02 17:30")
                response = self.client.get("/api/v1/posts/")
                actual = response.content
                expected_content = b'[{"title":"Peppa","content":"pig","author":null}]'
                self.assertEqual(actual, expected_content)
                self.assertEqual(response.status_code, 200)

        def test_get_author(self):
                Author.objects.create(name="Jose Buendia",email="jb@gmail.com")
                Author.objects.create(name="Florentino Ariza",email="fa@gmail.com")
                response = self.client.get("/api/v1/authors/")
                actual = response.content
                print(actual)
                expected_content = b'[{"name":"Jose Buendia","email":"jb@gmail.com"},{"name":"Florentino Ariza","email":"fa@gmail.com"}]'
                self.assertEqual(actual, expected_content)
                self.assertEqual(response.status_code, 200)
        
        def test_get_post_with_author(self):
                a = Author(name="Jose Buendia", email="jb@gmail.com")
                a.save()
                Post.objects.create(title="Peppa",content="pig",pub_date="1989-10-02 17:30", author=a)
                Post.objects.create(title="Papai",content="pig",pub_date="2024-10-02 17:30", author=a)
                response = self.client.get("/api/v1/posts/")
                actual = response.content
                expected_content = b'[{"title":"Peppa","content":"pig","author":"http://testserver/api/v1/authors/3/"},{"title":"Papai","content":"pig","author":"http://testserver/api/v1/authors/3/"}]'
                self.assertEqual(actual, expected_content)
                self.assertEqual(response.status_code, 200)
                
        