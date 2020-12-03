from django.urls import path
from . import views
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('clubs/', views.ClubListView.as_view(), name='clubs'),
    path('club/<int:pk>', views.ClubDetailView.as_view(), name='club-detail'),
    path('leagues/', views.LeagueListView.as_view(), name='leagues'),
    # path('rankings/', views.RankingsListView.as_view(), name='rankings'),
    path('rankings/', views.RankingsSearchView, name='rankings'),
    path('pbs/', views.PBSearchView, name='pbs'),
    path('league/<int:pk>', views.LeagueDetailView.as_view(), name='league-detail'),
    path('athletes/', views.AthleteListView.as_view(), name='athletes'),
    path('athlete/<uuid:pk>', views.AthleteDetailView.as_view(), name='athlete-detail'),
    path('venues/', views.VenueListView.as_view(), name='venues'),
    path('venues/<uuid:pk>', views.VenueDetailView.as_view(), name='venue-detail'),
    path('seasons/', views.SeasonListView.as_view(), name='seasons'),
    path('seasons/<uuid:pk>', views.SeasonDetailView.as_view(), name='season-detail'),
    path('events/', views.EventListView.as_view(), name='events'),
    # Adding Urls
    # path('practice/', views.practice, name='practice'),
    path('AllParticipant/<uuid:pk>/', views.ListParticipant, name='AllParticipant'),
    path('addEvent/', views.AddEvent, name='addEvent'),
    path('AllEventResults/<uuid:pk>/', views.EventResult, name='AllResult'),
    path('AddResult/', views.AddRessult, name='AddResult'),
    path('AddResult/UpdateResult/<uuid:pk>', views.updateResult.as_view(), name='UpdateResult'),
    path('AthletePB/', views.Athletpb, name='athletePB'),
    path('AddPB/', views.AddPB.as_view(), name='addPB'),
    path('updatePB/<uuid:pk>', views.updatePB.as_view(), name='updatePB'),

    path('events/<uuid:pk>', views.EventDetailView, name='event-detail'),
    path('meetings/<uuid:pk>', views.MeetingDetailView.as_view(), name='meeting-detail'),
    path('seasonsRanking/', views.SeasonsRankingView.as_view(), name='seasonsRanking'),
    path('recalc_rankings/<uuid:pk>', views.recalc_rankings, name='recalc_rankings'),


]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



