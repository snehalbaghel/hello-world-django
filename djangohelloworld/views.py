from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def sayHello(request):
    return Response({'message': 'Hello world!'})

