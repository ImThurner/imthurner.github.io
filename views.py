from django.http import HttpResponse
from django.template import loader


def index():
    template = loader.get_template("miniport/index.html")
    return HttpResponse(template.render())