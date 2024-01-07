from .serializers import SuperuserSerializer, SuperuserRetrieveSerializer
from .models import Superuser
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework import status

# Create your views here.


class CreateSuperuserView(CreateAPIView):
    permission_classes = []
    serializer_class = SuperuserSerializer
    queryset = Superuser.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:

            if serializer.is_valid():
                self.perform_create(serializer)
                data = {
                    "message": "Superuser created successifully",
                    "data": serializer.data
                }

                return Response(data, status=status.HTTP_201_CREATED)

            return Response({"message": "Failed to create superuser, Validation error occured.", "error": serializer.errors}, 
                            status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            return Response({"message": "Failed to create superuser. Exception error occured", "error": str(e)}, 
                            status=status.HTTP_400_BAD_REQUEST)
        

class GetAllSuperusers(ListAPIView):
    permission_classes = []
    serializer_class = SuperuserRetrieveSerializer
    queryset = Superuser.objects.all()


class SuperuserReadUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = []
    serializer_class = SuperuserRetrieveSerializer
    queryset = Superuser.objects.all()

