import json
from django.http import JsonResponse

def api_home(request,*args,**kwargs):
    # request -> HttpRequest -> Django
    # print(dir(request))

    body = request.body # byte string of JSON data
    data = {}
    try:
        data = json.loads(body) # JSON Data -> Python dict
    except:
        pass
    data['params'] = dict(request.GET)
    print(data)
    return JsonResponse({"message":"Hi there,this is your Django API response !!"})