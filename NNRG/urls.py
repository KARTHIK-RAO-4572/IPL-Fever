from django.urls import path
from . import views
urlpatterns = [
    path('',views.view_page),
    path('teams/',views.view_teams),
    path('squad/',views.view_squad),
    path('points/',views.view_points),
    path('stats/',views.view_stats),
    path("dashboard/",views.view_dashboard),
    path('send/',views.send_email_points)
]