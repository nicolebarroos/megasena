from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from game.serializer import PLaysSerializer
from game.models import Plays


class PLaysViewSet(viewsets.ModelViewSet):
    queryset = Plays.objects.all()
    serializer_class = PLaysSerializer
    permission_classes = (IsAuthenticated, )

