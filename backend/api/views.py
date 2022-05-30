import json
from django.http import JsonResponse
from django.forms.models import model_to_dict
from products.models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer

# This view function to show what request return and holds


def api_return_dict(request, *args, **kwargs):
    # request -> HttpRequest -> Django
    # print(dir(request))
    body = request.body  # byte string of JSON data
    data = {}
    try:
        data = json.loads(body)  # JSON Data -> Python dict
    except:
        pass
    data['params'] = dict(request.GET)
    print(data)
    return JsonResponse({"message": "Hi there,this is your Django API response !!"})


@api_view(["GET"])
def api_using_model_object_without_serializer(request, *args, **kwargs):
    """
    DRF API VIEW
    """
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        # this model convert our fetch to Python dict and we can filter the fields returned
        data = model_to_dict(model_data, fields=['id', 'title'])
    return Response(data)

@api_view(["GET"])
def api_home(request, *args, **kwargs):
    """
    DRF API VIEW
    """
    instance = Product.objects.all().order_by("?").first()
    data = {}
    if instance:
        # this product serialize will pass the object to class serializer and get the data of this instance
        data = ProductSerializer(instance).data
    return Response(data)
