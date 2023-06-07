from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Industry

class ImportantListsAPIView(APIView):
    
    def get(self, request):

        industry = Industry.objects.all()
        
        data = {
            "industry": industry,
        }
        
        return Response(data=data)  # Replace `data` with the response data you want to send back
