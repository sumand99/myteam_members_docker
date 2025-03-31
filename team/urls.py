from django.urls import path
from .views import TeamMemberListCreateView, TeamMemberRetrieveUpdateDestroyView

urlpatterns = [
    path('', TeamMemberListCreateView.as_view(), name='team_member_list_create'),
    path('<int:pk>/', TeamMemberRetrieveUpdateDestroyView.as_view(), name='team_member_detail'),
]
