from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from .models import Delegate
from .serializers import DelegateSerializer


@method_decorator(csrf_exempt, name='dispatch')
class DelegateCreateAPIView(generics.CreateAPIView):
    queryset = Delegate.objects.all()
    serializer_class = DelegateSerializer
    parser_classes = (MultiPartParser, FormParser)
