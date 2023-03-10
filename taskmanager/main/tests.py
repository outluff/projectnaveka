from django.template import RequestContext


def csrf(request):
    return render_to_response('main/login.html', {'form': c['login']},  RequestContext(request))
