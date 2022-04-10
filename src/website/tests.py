from django.test import TestCase
from . import models

import uuid
# Create your tests here.
class NewMessageTest(TestCase):
    def setUp(self):
        self.id = uuid.uuid4()
        models.Contacted.objects.create(
           subject ="Hello World",
            message="hello everyhting",
            sender="mellfang36@gmail.com",
            id = self.id )
    def test_got_it_questionmark(self):
        msg = models.Contacted.objects.get(sender="mellfang36@gmail.com")
        assert msg.sender == "mellfang36@gmail.com"
        assert msg.subject == "Hello World"
        assert msg.id == self.id
        """
    subject = models.CharField(max_length=100)
    message = models.CharField()
    sender = models.EmailField()
    id = models.UUIDField('id')
    
        """