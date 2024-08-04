from django.http import HttpResponse,JsonResponse

def http_test(request):
    return HttpResponse('http_test')

def json_test(request):
    return JsonResponse({'name': 'amir'})