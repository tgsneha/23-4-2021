from django.http import HttpResponse

def sample(request):
    return HttpResponse("hello world")


def sample1(request): 
    return HttpResponse("hello guys how are you")


