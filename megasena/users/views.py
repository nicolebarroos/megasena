from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from users.models import Users
from users.serializer import UsersSerializer


@api_view(['POST'])
def create_user(request):
    name = request.data['name']
    email = request.data['email']
    password = request.data['password']

    try:
        Users.objects.create_user(
            username=name,
            email=email,
            password=password
        )
        return Response({'Message': 'Usuário criado com sucesso'}, status=status.HTTP_201_CREATED)

    except Exception as e:
        return Response({'Message': 'Falha ao criar usuário'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def user_list(request):

    try:
        users = Users.objects.all()
        serializer = UsersSerializer(users, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk):
    if request.user.is_staff:
        try:
            user = Users.objects.get(pk=pk)
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = UsersSerializer(user)
            return Response(serializer.data)

        elif request.method == 'PUT':
            serializer = UsersSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response({'Message': 'Você não tem essa permissão'}, status=status.HTTP_401_UNAUTHORIZED)