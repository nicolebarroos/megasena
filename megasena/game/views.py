from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from game.models import Plays
from game.serializer import PLaysSerializer
from utils import get_results
import numpy as np
from datetime import datetime


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def generate_dozens(request):
    dozens = request.data['dozens']
    user = request.user
    try:
        list_dozens = np.random.randint(1, 60, (dozens))
        Plays.objects.create(
            dozens=list_dozens,
            creation_date=datetime.now(),
            user=user
        )
        return Response({'Dezenas geradas': list_dozens})
    except Exception as e:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def play_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        plays = Plays.objects.all()
        serializer = PLaysSerializer(plays, many=True)
        return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def play_game(request):
    user = request.user
    try:
        get_dozens = Plays.objects.filter(user=user).values()
        last_dozen = get_dozens[0]['dozens']
        result_megasena = get_results()
        if last_dozen == result_megasena:
            return Response({'Message': 'Você acertou!'})
        else:
            return Response({'Message': 'Você errou!'})
    except Exception:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def plays_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        play = Plays.objects.get(pk=pk)
    except Exception:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PLaysSerializer(play)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PLaysSerializer(play, data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        play.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)