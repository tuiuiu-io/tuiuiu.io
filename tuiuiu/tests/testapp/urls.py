from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from tuiuiu.tests.testapp.views import bob_only_zone, message_test

urlpatterns = [
    url(r'^bob-only-zone$', bob_only_zone, name='testapp_bob_only_zone'),
    url(r'^messages/$', message_test, name='testapp_message_test')
]
