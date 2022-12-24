import datetime
import time

from .models import NewStats
from django.db.models import F


class TestMiddleWare:
    def __init__(self, get_response):
        self.get_response = get_response
        self.new_data = 'POGGERS'

    def stats(self, user_agent_http):
        if 'Windows' in user_agent_http:
            NewStats.objects.all().update(win=F('win') + 1)
        elif 'Mac' in user_agent_http:
            NewStats.objects.all().update(win=F('mac') + 1)
        elif 'Android' in user_agent_http:
            NewStats.objects.all().update(win=F('android') + 1)
        elif 'CPU iPhone' in user_agent_http:
            NewStats.objects.all().update(win=F('iphone') + 1)
        else:
            NewStats.objects.all().update(win=F('win') + 1)

    def __call__(self, request):

        self.stats(request.META['HTTP_USER_AGENT'])

        response = self.get_response(request)
        return response

    def process_template_response(self, request, response):
        response.context_data['new_data'] = datetime.datetime.now()
        return response
