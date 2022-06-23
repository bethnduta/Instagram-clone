from django.test import TestCase

from django.contrib.auth.models import User

from .models import Post,profile



# Create your tests here.
class ProfileTestClass(TestCase):
    def test_is_true(self):
        self.assertTrue(True)

    def tearDown(self) :
        profile.objects.all().delete()
        Post.objects.all().delete() 

    def test_instance(self):
        self.assertTrue(isinstance(self.post, Post)) 



class PostTestClass(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='beth', email='beth@gmail.com', password='1234')
        self.post = Post.objects.create(user=self.user, image='nt.png', name='img', caption='nice image' )
    
    def test_instance(self):
        self.assertTrue(isinstance(self.post,Post))

    def test_save(self): 
        self.user.save()
        all_posts = Post.objects.all()
        self.assertEquals(len(all_posts),1)

    def test_delete(self):
        self.user.save()
        self.new_post = Post.objects.create(user=self.user, image='nt.png', name='img', caption='good' )
        self.new_post.save()
        self.new_post.delete()
        all_posts = Post.objects.all()
        self.assertEquals(len(all_posts),1)


        