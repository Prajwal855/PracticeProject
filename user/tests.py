from django.test import TestCase
import views


# Create your tests here.
class TestClac(TestCase):

    def test_add_profile(self):
        self.assertEquals(views.HelloAPIView.get(request='get'),200)
        pass