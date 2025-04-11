from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView

from .forms import AnswerForm, QuestionForm
from .models import Answer, Question


def home(request):
    """home screen view.

    Args:
        request (WSGIRequest): request object received from client

    Returns:
        HTMLTemplate: HTML template for client with desire output
    """
    return render(request, "base.html")


class HomeView(ListView):
    """Generic class view that shows list of questions

    Args:
        ListView (GenericView): Django inbuilt view to list objects
    """

    model = Question
    template_name = "home.html"
    context_object_name = "questions"


class QuestionCreateView(LoginRequiredMixin, CreateView):
    """Generic class view to create question using model form

    Args:
        LoginRequiredMixin (MixinClass): Mixin that adds login require constrain
        CreateView (GenericView): Django inbuilt generic view to create instance

    Returns:
        HTMLTemplate: return html template for client
    """

    model = Question
    form_class = QuestionForm
    template_name = "create.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.user = self.request.user.username
        return super().form_valid(form)


class QuestionDetailView(DetailView):
    """Generic detail view to return info of require object using primary key

    Args:
        DetailView (GenericView):Django inbuilt view

    Returns:
        HTMLTemplate: returns html template for client
    """

    model = Question
    template_name = "detail.html"
    context_object_name = "question"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["answers"] = Answer.objects.filter(question_id=self.object)
        context["form"] = AnswerForm()

        likes_count = {}
        is_liked = {}
        for answer in context["answers"]:
            if answer:
                likes = answer.likes.split("-")
                if likes[0]:
                    likes_count[answer.id] = len(likes)
                else:
                    likes_count[answer.id] = 0
                if user := self.request.user:
                    if str(user.id) in likes:
                        is_liked[answer.id] = True
                    else:
                        is_liked[answer.id] = False

        context["likes_count"] = likes_count
        context["is_liked"] = is_liked
        return context

    @method_decorator(login_required())
    def post(self, request, *args, **kwargs):
        """function to save answer submitted by user

        Args:
            request (WSGIRequest): request object received from client

        Returns:
            HTMLTemplate: HTML template for client with desire output
        """
        self.object = self.get_object()
        form = AnswerForm(request.POST)

        if form.is_valid():
            answer = form.save(commit=False)
            answer.question_id = self.object
            answer.user = request.user.username
            answer.save()
            return redirect("detail", pk=self.object.pk)
        else:
            context = self.get_context_data()
            context["form"] = form
            return self.render_to_response(context)


@login_required()
def like(request, question_pk, answer_pk):
    """Function that adds user id in likes for answer

    Args:
        request (WSGIRequest): request object received from client
        question_pk (int): primary key of question
        answer_pk (int): primary key of answer

    Returns:
        HTMLTemplate: HTML template for client with desire output
    """
    answer = Answer.objects.get(pk=answer_pk)
    user_id = str(request.user.id)
    if answer.likes:
        answer.likes += "-" + user_id
    else:
        answer.likes = user_id
    answer.save()
    return redirect("detail", pk=question_pk)
