from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny

from base.models import Team,User
from .serializers import TeamSerializer,UserSerializer,addTeamSerializer

# Create your views here.



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getName(request):
    team = Team.objects.all()
    serializer = TeamSerializer(team, many=True)
    return Response(serializer.data)


class TeamCreateAPIView(generics.CreateAPIView):
    queryset = Team.objects.all()
    serializer_class = addTeamSerializer
    permission_classes = (IsAuthenticated,)


class GetUserAccount(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    # def get_queryset(self):
    #     queryset = self.queryset
    #     query_set = queryset.all()
    #     return query_set


class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
