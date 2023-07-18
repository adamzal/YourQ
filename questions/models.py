from django.db import models
from django.utils.translation import gettext_lazy as _
from quizzes.models import Quiz
# Create your models here.


class Question(models.Model):

    class CorectAnswer(models.TextChoices):
        A = "A", _("A")
        B = "B", _("B")
        C = "C", _("C")
        D = "D", _("D")

    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    text = models.CharField(_("text"), max_length=200)
    answer_a = models.CharField(_("answer A"), max_length=50)
    answer_b = models.CharField(_("answer B"), max_length=50)
    answer_c = models.CharField(_("answer C"), max_length=50)
    answer_d = models.CharField(_("answer D"), max_length=50)
    correct_answer = models.CharField(_("correct answer"),max_length=1, choices=CorectAnswer.choices)
    is_correct = models.BooleanField(_("is correct"), default=False)

    def __str__(self):
        return f'{self.quiz} - {self.text}'