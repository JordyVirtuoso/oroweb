from rest_framework.views import APIView # structure our view with APIView attributes
from rest_framework.response import Response # our responses will be RESTful
from rest_framework import status
from rest_framework import permissions
from oro.models import Item
from .serializers import ItemSerializer


class ItemApiView(APIView):
    # require authentication to make calls
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        # get all Item objects from database
        items = Item.objects.all()
        # serialize the objects
        serializer = ItemSerializer(items, many=True)
        
        # give back response with requested data
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        # data will be an object with a name attribute, and will be linked to User by their id
        data = {
            'name': request.data.get('name'),
            'user': request.user.id
        }
        # data is serialized and stored
        serializer = ItemSerializer(data=data)
        if serializer.is_valid():
            serializer.save()

            # give back response with new data
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        # triggers if error with creating data, returns response with said error
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)