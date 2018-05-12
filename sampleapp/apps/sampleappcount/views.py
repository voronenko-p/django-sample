from django.shortcuts import render
from sampleappcount.models import Visit
import platform

def say_hello(request):
    user_agent = request.META['HTTP_USER_AGENT']
    python_version = platform.python_version()
    Visit.objects.create(user_agent=user_agent)
    return render(request, 'say_hello.html', {
        'count': Visit.objects.count(),
        'user_agent': user_agent,
        'python_version': python_version
    })
