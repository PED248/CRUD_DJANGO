from django.test import TestCase
from . models import task
from django.contrib.auth.models import User
# Create your tests here.


class ModelTesting(TestCase):
    def setUp(self):
        self.tasks = task.objects.create(
            title='django', description='django', important=False, user="1" "task.user")

    def test_task_model(self):
        dt = self.tasks
        self.assertTrue(isinstance(dt, task))
