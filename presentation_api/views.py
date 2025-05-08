from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Presentation
from .serializers import PresentationSerializer


class PresentationView(APIView):
    def get(self, request):
        try:
            presentation = Presentation.objects.first()
            serializer = PresentationSerializer(
                presentation, context={'request': request})
            return Response(serializer.data)
        except Presentation.DoesNotExist:
            return Response({'error': 'No presentation found'}, status=404)
