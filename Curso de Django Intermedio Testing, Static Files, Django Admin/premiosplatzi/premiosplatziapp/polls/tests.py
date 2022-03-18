import datetime
from urllib import response

from django.test import TestCase
from django.urls. base import reverse
from django.utils import timezone

from .models import Question

# Vistas

# Models
class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_questions(self):
        """was_published_recently returns False for questions whose pub_date is the future"""
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(question_text="¿Quién es el mejor Course Director de Platzi?", pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_present_questions(self):
        """was_published_recently returns False for questions whose pub_date is the present"""
        time = timezone.now() 
        present_question = Question(question_text="¿Quién es el mejor Course Director de Platzi?", pub_date=time)
        self.assertIs(present_question.was_published_recently(), True)

    def test_was_published_recently_with_past_questions(self):
        """was_published_recently returns False for questions whose pub_date is the past"""
        time = timezone.now() - datetime.timedelta(days=1.0001)
        past_question = Question(question_text="¿Quién es el mejor Course Director de Platzi?", pub_date=time)
        self.assertIs(past_question.was_published_recently(), False)


def create_question(question_text, days):
    """
    Crete a question with the given "question_text", and published the given number of days offset to now (negative for questions published in the past, positive for questions that have yet to be published)
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionIndexViewTest(TestCase):

    def test_no_questions(self):
        """If no question exist, an appropiate massage is displayed"""
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context["latest_question_list"], [])
    
    # def test_questions_with_future_pub_date(self):
    #     """
    #         Questions with a pub_date later than the current date should not appear in the index view.
    #     """
    #     Question(question_text='Present Question', pub_date=timezone.now()).save()
    #     Question(question_text='Future Question', pub_date=timezone.now() + datetime.timedelta(days=30)).save()

    #     response = self.client.get(reverse('polls:index'))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertContains(response, "Present Question")
    #     self.assertNotContains(response, "Future Question")

    def test_future_question(self):
        """
        Question with a pub_date in the future aren't displayed on the index page.
        """
        create_question("Future question", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context["latest_question_list"], [])

    def test_pass_question(self):
        """
        Questions with a pub_date in the past are displayed on the index page
        """
        question = create_question("Past question", days=-10)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(response.context["latest_question_list"], [question])