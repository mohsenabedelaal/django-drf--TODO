import json
from django.http import JsonResponse
from products.models import Product

def api_test(request,*args,**kwargs):
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

def api_home(request,*args,**kwargs):
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data['id'] = model_data.id
        data['title'] = model_data.title
        data['content'] = model_data.content
        data['price'] = model_data.price
    return JsonResponse(data)