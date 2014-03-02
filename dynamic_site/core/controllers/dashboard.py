# coding: utf-8
from django.shortcuts import render_to_response, render
from django.template import RequestContext

HOME_PAGE = 'home.html'

def home(request):
    """
    公司主页
    :param request:
    :return:
    """
    # latest_tabs = models.Tab.objects.filter().order_by('-created_at')[:20]
    # url_pre = 'http://' + request.META["HTTP_HOST"] + '/tab/show_detail/'
    return render(request, 'kunyutex/index.html', {})
