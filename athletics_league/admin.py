from django.contrib import admin
# Register your models here.

from .models import Athlete, Club, League, Meeting, Venue, Event, Season, EventParticipant ,TrackEventResult, FieldEventResult, Speciality, AthleteRanking, AgeGroup, Coach, AthletePB,Gender, SpecialityType, EventRound

# admin.site.register(Athlete)
# admin.site.register(Club)
admin.site.register(League)
admin.site.register(Speciality)
admin.site.register(Meeting)
admin.site.register(Venue)
admin.site.register(Event)
admin.site.register(TrackEventResult)
admin.site.register(FieldEventResult)
admin.site.register(AthleteRanking)
admin.site.register(AgeGroup)
admin.site.register(Coach)
admin.site.register(AthletePB)
admin.site.register(Gender)
admin.site.register(SpecialityType)
admin.site.register(EventRound)

#admin.site.register(EventParticipant)


# Define the admin class
class AthletePB(admin.ModelAdmin):
     list_display = ('Athlete', 'Speciality', 'Season', 'AgeGoup','Gender','PB_Date','pb_time')
     
class AthleteAdmin(admin.ModelAdmin):
     list_display = ('Athlete_Name', 'Athlete_Surname', 'Date_of_birth', 'Club')
     list_filter = ('Athlete_Gender', 'AgeGroup', 'Club')

class EventParticipantAdmin(admin.ModelAdmin):
     list_display = ('Event', 'Athlete', 'bib', 'lane')
     list_filter = ('Event',)

     
class ClubAdmin(admin.ModelAdmin):
     list_display = ('Club_Name','League')
     list_filter = ('League',)
     
class LeagueAdmin(admin.ModelAdmin):
     list_display = ('Club','Athlete_Name')

class SeasonAdmin(admin.ModelAdmin):
     list_display = ('season_year', 'season_Name')

"""class EventAdmin(admin.ModelAdmin):
     list_display = ('event_name')"""
# Register the admin class with the associated model
admin.site.register(Athlete, AthleteAdmin)
admin.site.register(EventParticipant, EventParticipantAdmin)
admin.site.register(Club, ClubAdmin)
admin.site.register(Season, SeasonAdmin)
"""admin.site.register(Event, EventAdmin)"""
"""admin.site.register(League, LeagueAdmin)"""
#@admin.register(BookInstance)
class AthleteTimesAdmin(admin.ModelAdmin):
    list_display = ('Athlete', 'Club', 'Event_Result', 'Event')
    list_filter = ('Event', 'Club')
    
    fieldsets = (
        (None, {
            'fields': ('book','imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back','borrower')
        }),
    )




