from django import forms
from .models import EventParticipant,TrackEventResult,AthletePB


class EventParticipantModel(forms.ModelForm):
    
    class Meta:
        model = EventParticipant
        fields = ['Event','Athlete','bib','lane']

class EventTrackModel(forms.ModelForm):
    
    class Meta:
        model = TrackEventResult 
        fields = ['EventParticipant','duration']

class AthletePBModel(forms.ModelForm):
    
    class Meta:
        model = AthletePB
        fields = ['Speciality','Athlete','Season','AgeGroup','Gender','Speciality_Type','PB_Date','pb_time','PB']