# coding: utf-8
from django.http import HttpResponse
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from dynamic_site import settings

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

def flash(request):
    """
    获取首页大flash所原来的xml
    :param request:
    :return:
    """
    flash_xml_data = open(settings.BASE_DIR + "/dynamic_site/static/kunyutex/flash/xml/focus_pics.xml", "rb").read()
    return HttpResponse(flash_xml_data, mimetype="application/xml")
