from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from game.models import Plays
from game.serializer import PLaysSerializer
from utils import get_results
import random
from datetime import datetime


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def play_game(request):
    #user informs the number of tens he wants to try his luck
    dozens = request.data['dozens']
    user = request.user
    try:
        #a list of random numbers from 1 to 60 is created, the size of the list is equivalent to the number of tens entered
        list_dozens = random.sample(range(1,61),dozens)
        #here we call the script that performs the webscraping and store the mega result in a variable
        result_megasena = get_results()

        #we create an object containing the user's move
        Plays.objects.create(
            first_dozen=list_dozens[0],
            second_dozen=list_dozens[1],
            third_dozen=list_dozens[2],
            fourth_dozen=list_dozens[3],
            fifth_dozen=list_dozens[4],
            sixth_dozen=list_dozens[5],
            creation_date=datetime.now(),
            user=user
        )
        #here we check if the user has hit at least four mega sena numbers (according to the official game rules)
        total_result = []
        for i in result_megasena:
            for j in list_dozens:
                if i == j:
                    total_result.append(i)
        if len(total_result) >= 4:
            return Response({'Você acertou o número mínimo de combinações: ': total_result})
        else:
            return Response({'Segue os resultados da mega sena': result_megasena,
                             'Seus resultados ': list_dozens})

    except Exception as e:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def play_list(request):
    if request.user.is_staff:
        plays = Plays.objects.filter(user=request.user)
        serializer = PLaysSerializer(plays, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE'])
def plays_detail(request, pk):

    try:
        play = Plays.objects.get(pk=pk)
    except Exception:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PLaysSerializer(play)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        play.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)