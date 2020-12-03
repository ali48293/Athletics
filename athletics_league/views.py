from django.shortcuts import render
from django.contrib import messages

# Create your views here.
from .models import Club, Athlete, League, Venue, Season, Event, Meeting, EventParticipant, AthleteRanking, AthletePB,TrackEventResult

from .filters import RankingFilter
from .filters import PBFilter

from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import EventParticipantModel,EventTrackModel,AthletePBModel


def ListParticipant(request,pk):
    # events = EventParticipant.objects.all()
    event_obj = EventParticipant.objects.select_related('Athlete').filter(Event=pk)
    
    return render(request,'athletics_league/AllParticipant.html',{'event_obj':event_obj}) 



def AddEvent(request):
    
    if request.method == 'POST':
       
        track_finalist =request.POST.get('Event') 
        
        event_obj = EventParticipant.objects.select_related('Athlete').filter(Event=track_finalist)
        EventModel =   EventParticipantModel(request.POST)
        if EventModel.is_valid():
            EventModel.save()
            return redirect('AllParticipant',track_finalist)
    else:
        EventModel = EventParticipantModel()
    # print("All Objects: " ,event_obj)
    return render(request,'athletics_league/addEvent.html',{'Form':EventModel})      
   

def EventResult(request,pk):
    track  = TrackEventResult.objects.all()
    event_obj =  event_obj =TrackEventResult.objects.filter(EventParticipant=pk)
    

    return render(request,'athletics_league/AllResults.html',{'track':track,'eventresult':event_obj})    

 
 
def AddRessult(request):

    if request.method == 'POST':
    
        track_finalist =request.POST.get('EventParticipant') 
    
        event_obj =TrackEventResult.objects.filter(EventParticipant=track_finalist)
        
        EventModel = EventTrackModel(request.POST)
        if EventModel.is_valid():
            EventModel.save()
            
            return redirect('AllResult',track_finalist)
    else:
        EventModel = EventTrackModel()
    
    return render(request,'athletics_league/addResult.html',{'Form':EventModel})      
    
    
class updateResult(generic.UpdateView):
    model =TrackEventResult
    template_name = 'athletics_league/updateResult.html'
    form_class = EventTrackModel
    success_url = reverse_lazy('AllResult')    
    

def Athletpb(request):
    athletes = AthletePB.objects.all()[:4]
    filAth = AthletePB.objects.order_by('pb_time')[:2]
    context = {
        'athlete':athletes,
        'filtered':filAth
    }
    return render(request,'athletics_league/athlete_list.html',context)   
    
class AddPB(generic.CreateView):
    model = AthletePB
    form_class = AthletePBModel
    template_name = 'athletics_league/Addathlete_pb.html'
    success_url = reverse_lazy('athletePB')
    
class updatePB(generic.UpdateView):
    model =AthletePB
    template_name = 'athletics_league/updatePB.html'
    form_class = AthletePBModel
    success_url = reverse_lazy('athletePB')    

class ClubListView(generic.ListView):
    model = Club

class ClubDetailView(generic.DetailView):
    model = Club

class LeagueListView(generic.ListView):
    model = League

class LeagueDetailView(generic.DetailView):
    model = League

class AthleteListView(generic.ListView):
    model = Athlete

class AthleteDetailView(generic.DetailView):
    model = Athlete

class VenueListView(generic.ListView):
    model = Venue

class VenueDetailView(generic.DetailView):
    model = Venue

class SeasonListView(generic.ListView):
    model = Season

class RankingsListView(generic.ListView):
    model = AthleteRanking
  
def RankingsSearchView(request):
    model = AthleteRanking.objects.all()
    myFilter = RankingFilter(request.GET, queryset=AthleteRanking.objects.all().order_by('-ranking'))
    model = myFilter.qs
    context = {
        'rankings': model,
        'filter': myFilter}
    
    #return render(request,'athletics_league/athleteranking_list.html',{'filter': myFilter})
    return render(request,'athletics_league/athleteranking_list.html',context=context)

def PBSearchView(request):
    if(request.GET.get('recalc')):
        print("Recalculating rankings....")
        # make sure age group/seasons are selected, else return to page
        
    model = AthletePB.objects.all()
    myFilter = PBFilter(request.GET, queryset=AthletePB.objects.all())
    model = myFilter.qs.order_by('-PB__duration')
    #model = myFilter.qs
    context = {
        'pbs': model,
        'filter': myFilter}

    ranking = 1
    #for athletepb in model:
        #find ranking corresponding to this?
     #   ranking += 1
    
    #return render(request,'athletics_league/athleteranking_list.html',{'filter': myFilter})
    return render(request,'athletics_league/athletepb_list.html',context=context)


class SeasonDetailView(generic.DetailView):
    model = Season
    
class EventListView(generic.ListView):
    model = Event

# class EventDetailView(generic.DetailView):
#     model = Event
#     def get_context_data(self, **kwargs):
    
            
#         context = super().get_context_data(**kwargs)
#         Meeting_id = Event.objects.get(event_id=pk)
    
#         context['Event'] = Event.objects.all()
#         context['Participant'] = TrackEventResult.objects.order_by('duration')[:2]
#         return context

def EventDetailView(request,pk):
            

        event_qs = EventParticipant.objects.filter(Event=pk)
        
        for i in event_qs:
            # print(i)
            for j in i.trackeventresult_set.all():
                    print(j.EventParticipant)
                    # print(j.duration)
                    
       


        context ={
            
            'Participant': event_qs} 
        return render(request,'athletics_league/event_detail.html',context)

class MeetingDetailView(generic.DetailView):
    model = Meeting

from django.contrib.auth.mixins import LoginRequiredMixin

class SeasonsRankingView(LoginRequiredMixin,generic.ListView):
    model = Season
    template_name ='athletics_league/season_ranking_list.html'
    def get_queryset(self):
        return Season.objects.all()

from django.http import HttpResponseRedirect
from django.shortcuts import redirect

def recalc_rankings(request, pk):
    # contact = Contact.objects.get(pk=pk)
    # contact.last_contacted = timezone.now()
    #contact.save()
    #return reverse("contact_list")
    model = AthleteRanking.objects.all()
    myFilter = RankingFilter(request.GET, queryset=AthleteRanking.objects.all().order_by('-ranking'))
    model = myFilter.qs
    model = AthletePB.filter
    return redirect('index')

def search_ranking(request):
    f = RankingFilter(request.GET, queryset=AthleteRanking.objects.all().order_by('-ranking'))
    return render(request, 'athletics_league/rankings.html', {'filter': f})

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_clubs = Club.objects.all().count()
    num_athletes = Athlete.objects.all().count()
    num_leagues = League.objects.all().count()
    num_venues = Venue.objects.all().count()
    num_seasons = Season.objects.all().count()
    num_events = Season.objects.all().count()
    context = {
        'num_clubs': num_clubs,
        'num_athletes': num_athletes,
        'num_leagues': num_leagues,
        'num_venues': num_venues,
        'num_seasons': num_seasons,
        'num_events': num_events,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

from .models import TrackEventResult,EventParticipant,EventRound,Athlete
