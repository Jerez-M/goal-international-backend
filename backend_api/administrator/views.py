from .serializers import AdministratorSerializer, AdministratorRetrieveSerializer
from .models import Administrator
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework import status

# Create your views here.


class CreateAdministratorView(CreateAPIView):
    permission_classes = []
    serializer_class = AdministratorSerializer
    queryset = Administrator.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:

            if serializer.is_valid():
                self.perform_create(serializer)
                data = {
                    "message": "Administrator created successifully",
                    "data": serializer.data
                }

                return Response(data, status=status.HTTP_201_CREATED)

            return Response({"message": "Failed to create administrator, Validation error occured.", "error": serializer.errors}, 
                            status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            return Response({"message": "Failed to create administrator. Exception error occured", "error": str(e)}, 
                            status=status.HTTP_400_BAD_REQUEST)
        

class GetAllAdministrators(ListAPIView):
    permission_classes = []
    serializer_class = AdministratorRetrieveSerializer
    queryset = Administrator.objects.all()


class AdministratorReadUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = []
    serializer_class = AdministratorRetrieveSerializer
    queryset = Administrator.objects.all()

