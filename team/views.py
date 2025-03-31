from rest_framework import generics
from .models import TeamMember
from .serializers import TeamMemberSerializer

# List all team members or create a new member
class TeamMemberListCreateView(generics.ListCreateAPIView):
    queryset = TeamMember.objects.all().order_by('id')
    serializer_class = TeamMemberSerializer

# Retrieve, update, or delete a specific team member
class TeamMemberRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer