from .serializers import GeneralEmployeeSerializer, GeneralEmployeeRetrieveSerializer
from .models import GeneralEmployee
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework import status

# Create your views here.


class CreateGeneralEmployeeView(CreateAPIView):
    permission_classes = []
    serializer_class = GeneralEmployeeSerializer
    queryset = GeneralEmployee.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:

            if serializer.is_valid():
                self.perform_create(serializer)
                data = {
                    "message": "general employee created successifully",
                    "data": serializer.data
                }

                return Response(data, status=status.HTTP_201_CREATED)

            return Response({"message": "Failed to create general employee, Validation error occured.", "error": serializer.errors}, 
                            status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            return Response({"message": "Failed to create general employee. Exception error occured", "error": str(e)}, 
                            status=status.HTTP_400_BAD_REQUEST)
        

class GetAllGeneralEmployees(ListAPIView):
    permission_classes = []
    serializer_class = GeneralEmployeeRetrieveSerializer
    queryset = GeneralEmployee.objects.all()


class GeneralEmployeeReadUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = []
    serializer_class = GeneralEmployeeRetrieveSerializer
    queryset = GeneralEmployee.objects.all()

