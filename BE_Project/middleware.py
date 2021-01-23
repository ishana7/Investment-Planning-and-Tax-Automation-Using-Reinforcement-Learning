import re
from django.conf import settings
from django.urls import reverse_lazy
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth import logout

EXEMPT_URLS = [re.compile(settings.LOGIN_URL.lstrip('/'))]
if hasattr(settings, 'LOGIN_EXEMPT_URLS'):
    EXEMPT_URLS += [re.compile(url) for url in settings.LOGIN_EXEMPT_URLS]


class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    #def exempturls(self, request):
        #EXEMPT_URLS = () + (settings.LOGIN_URL.lstrip('/'),)
        #LOGIN_EXEMPT_URLS = (
           # reverse_lazy('register'),
           # reverse_lazy('home'),
           # reverse_lazy('reset-password'),
           # reverse_lazy('reset_password_done'),
            #reverse_lazy('reset_password_confirm'),
           # reverse_lazy('reset_password_complete'),
        #)

        #for i in LOGIN_EXEMPT_URLS:
            #EXEMPT_URLS += (i.lstrip('/'),)

        #return EXEMPT_URLS

    def process_view(self, request, view_func, view_args, view_kwargs):
        assert hasattr(request, 'user')  #to check if request.user exists
        path = request.path_info.lstrip('/')

        #if path in EXEMPT_URLS or path[0:len("account/reset_password/confirm/")] == "account/reset_password/confirm/":
            #url_is_exempt = True
        #else:
            #url_is_exempt = False

        #if not request.user.is_authenticated:
            #if not any(url.match(path) for url in EXEMPT_URLS):
                #return redirect(settings.LOGIN_URL)

        url_is_exempt = any(url.match(path) for url in EXEMPT_URLS)

        if path == reverse('logout').lstrip('/'):
            logout(request)

        #if (not request.user.is_authenticated and url_is_exempt) or (
                #request.user.is_authenticated and not url_is_exempt):
            #return None

        #elif not request.user.is_authenticated and not url_is_exempt:
            #return redirect(settings.LOGIN_URL)

        #else:
            #return redirect(settings.LOGIN_REDIRECT_URL)

        if request.user.is_authenticated and url_is_exempt:
            return redirect(settings.LOGIN_REDIRECT_URL)

        elif request.user.is_authenticated or url_is_exempt:
            return None

        else:
            return redirect(settings.LOGIN_URL)


