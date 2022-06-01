import datetime
from urllib import response

from django.test import TestCase
from django.urls.base import reverse
from django.utils import timezone

from .models import Question, Choice


# Models
def create_question(question_text, days):
    """
    Crete a question with the given "question_text", and published the given number of days offset to now 
    (negative for questions published in the past, positive for questions that have yet to be published)
    """
    time = timezone.now() + datetime.timedelta(days=days)
    
    question = Question(question_text=question_text, pub_date=time)
    choice1 = Choice(question=question,choice_text="Choice 1", votes=0)
    choice2 = Choice(question=question,choice_text="Choice 2", votes=0)
    question.save(choices=(choice1, choice2))
    return question


class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_questions(self):
        """was_published_recently returns False for questions whose pub_date is the future"""
        future_question = create_question(question_text="Future question", days=30)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_present_questions(self):
        """was_published_recently returns True for questions whose pub_date is the present"""
        present_question = create_question(question_text="Present question", days=0)
        self.assertIs(present_question.was_published_recently(), True)

    def test_was_published_recently_with_past_questions(self):
        """was_published_recently returns False for questions whose pub_date is the past"""
        past_question = create_question(question_text="Past question", days=-30)
        self.assertIs(past_question.was_published_recently(), False)

    def test_no_create_questions_without_choices(self):
        """no_create_questions rise a Error for questions create without choices"""
        question = Question(question_text="Question without choices", pub_date=timezone.now())
        with self.assertRaises(ValueError):
            question.save()
        

# Vistas
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


    def test_future_question_and_past_question(self):
        """
        Even if both past and future question exist, only past question are displayed
        """
        past_question = create_question(question_text="Past question", days=-30)
        future_question = create_question(question_text="Future question", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(
            response.context["latest_question_list"], [past_question]
        )

    def test_two_past_questions(self):
        """
        The question index page may display multiple question.
        """
        past_question1 = create_question(question_text="Past question 1", days=-30)
        past_question2 = create_question(question_text="Past question 2", days=-40)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(
            response.context["latest_question_list"], [past_question1, past_question2]
        )

    def test_two_future_question(self):
        """
        Question with a pub_date in the future aren't displayed multiple question on the index page.
        """
        future_question1 = create_question("Future question 1", days=30)
        future_question2 = create_question("Future question 2", days=10)
        response = self.client.get(reverse("polls:index"))
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context["latest_question_list"], [])


class QuetionDetailViewTests(TestCase):
    def test_future_question(self):
        """
        The datil view of a question whit a pub_date in the future returns a 404 error not found
        """
        future_question = create_question(question_text="Future question", days=30)
        url = reverse("polls:detail", args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        """
        The detail view of a question whit a pub_date in the past displays the question's text
        """
        past_question = create_question(question_text="Past question", days=-30)
        url = reverse("polls:detail", args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)

    
class ChoiceResultViewTests(TestCase):
    def test_question_not_exists(self):
        """ If question id not exists, get 404 """
        response= self.client.get(reverse("polls:results", kwargs={'pk':1}))
        self.assertEqual(response.status_code, 404)
    
    def test_result_right(self):
        """
        Page may display votes for every choice of a question.
        """
        time = timezone.now() + datetime.timedelta(days=1)
        question = Question(question_text="Present question", pub_date=time)
        choice1 = Choice(question=question,choice_text="Choice 1", votes=1)
        choice2 = Choice(question=question, choice_text="Choice 2")
        choice3 = Choice(question=question, choice_text="Choice 3")
        choice4 = Choice(question=question, choice_text="Choice 4")
        choice5 = Choice(question=question,choice_text="Choice 5")
        question.save(choices=(choice1, choice2,choice3, choice4, choice5))

        response = self.client.get(reverse("polls:results", kwargs={'pk': question.pk}))

        self.assertContains(response, question.question_text)
        self.assertContains(response, choice1.choice_text + ' -- ' + '1 vote' )
        self.assertContains(response, choice2.choice_text + ' -- ' + '0 votes' )
        self.assertContains(response, choice3.choice_text + ' -- ' + '0 votes' )
        self.assertContains(response, choice4.choice_text + ' -- ' + '0 votes' )
        self.assertContains(response, choice5.choice_text + ' -- ' + '0 votes' )