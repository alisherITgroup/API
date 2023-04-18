from .serializer import AttemptSerializer
from .models import Attempt
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
import requests
from problems.models import Problem
from json import dumps
from django.contrib.auth.models import User

class AttemptPagination(PageNumberPagination):
    page_query_param = "page"
    page_size = 50
    max_page_size = 50

class AttemptViewSet(ModelViewSet):
    queryset = Attempt.objects.all()
    serializer_class = AttemptSerializer
    pagination_class = AttemptPagination

    def create(self, request, *args, **kwargs):
        token = "7f3b28a781ba850296fbd5ec5578f1787aa9e772"
        url = "https://algorithmshubtestapi.pythonanywhere.com/test/"
        print(request.data)
        # try:
        request.POST._mutable = True
        code = request.data.get("code")
        language = request.data.get("language")
        problem = request.data.get("problem")
        author = request.data.get("author")
        user = User.objects.get(id=author)
        problem = Problem.objects.get(id=problem)
        payload = {
            "name": user.username,
            "code": str(code),
            "language": str(language),
            "tests": str(problem.tests),
            "timelimit": problem.timelimit
        }
        response = requests.post(
            url=url,
            data=payload,
            headers={
                "Authorization": f"Token {token}"
            }
        )
        result = response.json()
        time = result["time"]
        cases = result["results"]
        error = result["error"]
        status = result["status"]
        request.data["status"] = status
        request.data["cases"] = dumps(eval(cases))
        request.data["time"] = time
        request.data["error"] = error
        print(response)
        if type(request.data) != dict:
            request.data._mutable = False
        return super().create(request, *args, **kwargs)