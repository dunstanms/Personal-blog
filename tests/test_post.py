import unittest
from app.models import Post, User, Comment

class TestPost(unittest.TestCase):
    
    def setUp(self):
        self.user_Stan = User(first_name = "scott",
                                last_name = "parker",
                                username = "stan_m",
                                password = "easy",
                                email = "scott@mail.com")
        self.new_post = Post(post_title = "Sample Title",
                            post_content = "Hallo Welt! Ich bin hier",
                            user_id = self.user_Stan.id)
        self.new_comment = Comment(comment = "Nice job",
                                    post_id = self.new_post.id,
                                    user_id = self.user_Stan.id)

    def test_instance(self):
        self.assertTrue(isinstance(self.user_Stan, User))
        self.assertTrue(isinstance(self.new_post, Post))
        self.assertTrue(isinstance(self.new_comment, Comment))