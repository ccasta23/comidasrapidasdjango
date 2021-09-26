from django.http import HttpResponse

def hello_world(request, name, lastname):
    return HttpResponse(f'Hello {name} {lastname} 😁')

def debug_view(request):
    #import pdb; pdb.set_trace()
    numbers = request.GET['numbers']
    numbers = numbers.split(',')
    return HttpResponse(numbers)