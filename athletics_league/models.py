from django.db import models
from django.urls import reverse
import uuid
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator 
# Create your models here.

class AgeGroup(models.Model):
    AgeGroup_ID = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular Age Grop across whole league')
    AgeGroup_name = models.CharField(max_length=20)
    AgeGroup_description = models.CharField(max_length=40)
    def __str__(self):
        return self.AgeGroup_name
    def get_absolute_url(self):
        """Returns the url to access a detail record for this athlete."""
        return reverse('agegroup-detail', args=[str(self.AgeGroup_ID)])


class Coach(models.Model):
    Coach_ID = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular Coach across whole league')
    Coach_name = models.CharField(max_length=20)
    Coach_surname = models.CharField(max_length=20)
    def __str__(self):
        return self.Coach_name + ' ' + self.Coach_surname

class Gender(models.Model):
    Gender_ID = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular Gender')
    GENDER_TYPE= (
        ('M', 'Male'),
        ('F', 'Felmale'),
    )
    """possible gender options"""
    gender= models.CharField(
        max_length=1000000,
        choices=GENDER_TYPE,
        blank=True,
        default='M',
        help_text='Athlete Gender',
    )

    def __str__(self):
        return self.gender
    

class Athlete(models.Model):
    """what consists of"""
    Athlete_ID = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular Athlete across whole league')
    Club = models.ForeignKey('Club', on_delete=models.SET_NULL, null=True)
    AgeGroup = models.ForeignKey('AgeGroup', on_delete=models.SET_NULL, null=True)
    Coach = models.ForeignKey('Coach', on_delete=models.SET_NULL, null=True)
    Athlete_Name = models.CharField(max_length=20)
    Athlete_Surname = models.CharField(max_length=20)
    Athlete_email = models.EmailField
    Date_of_birth = models.DateField(null=True, blank=True)
    Athlete_Gender = models.ForeignKey('Gender', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        """ athlete full name"""
        return self.Athlete_Name + self.Athlete_Surname

    def get_absolute_url(self):
        """Returns the url to access a detail record for this athlete."""
        return reverse('athlete-detail', args=[str(self.Athlete_ID)])

class AthletePB(models.Model):
    AthletePB_ID = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular Personal Best')
    Speciality = models.ForeignKey('Speciality', on_delete=models.SET_NULL, null=True) 
    Athlete = models.ForeignKey('Athlete', on_delete=models.SET_NULL, null=True)
    Season = models.ForeignKey('Season', on_delete=models.SET_NULL, null=True)
    AgeGroup = models.ForeignKey('AgeGroup', on_delete=models.SET_NULL, null=True)
    Gender = models.ForeignKey('Gender', on_delete=models.SET_NULL, null=True)
    Speciality_Type = models.ForeignKey('SpecialityType', on_delete=models.SET_NULL, null=True)
    PB_Date = models.DateField(null=True, blank=True)
    pb_time = models.DurationField(null=True, blank=True)
    PB = models.ForeignKey('TrackEventResult', on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.PB_Date , self.pb_time , self.PB 

class Speciality(models.Model):
    Speciality_ID = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular Speciality across whole league')
    speciality_name = models.CharField(max_length=50)
    Speciality_Type = models.ForeignKey('SpecialityType', on_delete=models.SET_NULL, null=True)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['speciality_name'], name='unique speciality name'),
        ]

    def __str__(self):
        return self.speciality_name

class SpecialityType(models.Model):
    SpecialityType_ID = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular Speciality across whole league')
    speciality_type = (
        ('T', 'Track'),
        ('F', 'Field'),
    )
    Speciality_type = models.CharField(
        max_length=10000,
        choices=speciality_type,
        blank=True,
        default='T',
        help_text='speciality type',
    )

    def __str__(self):
        return self.Speciality_type

class AthleteRanking(models.Model):
    AthleteRanking_ID = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular Athlete Ranking across whole league')
    Athlete = models.ForeignKey('Athlete', on_delete=models.SET_NULL, null=True)
    Speciality = models.ForeignKey('Speciality', on_delete=models.SET_NULL, null=True)
    Season = models.ForeignKey('Season', on_delete=models.SET_NULL, null=True)
    ranking = models.PositiveIntegerField(default=1,validators=[MinValueValidator(1)],null=True, blank=True)
    AgeGroup = models.ForeignKey('AgeGroup', on_delete=models.SET_NULL, null=True)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['Athlete', 'Speciality', 'Season'], name='unique ranking per speciality per season'),
        ]

class Club(models.Model):
    """Club_ID = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular Club across whole league')"""
    League = models.ForeignKey('League', on_delete=models.SET_NULL, null=True)
    Club_Name = models.CharField(max_length=40)

    def __str__(self):
        """club name"""
        return self.Club_Name
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this club."""
        return reverse('club-detail', args=[str(self.id)])

class League(models.Model):
    League_ID = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular league')
    League_Name = models.CharField(max_length=40)

    def __str__(self):
        return self.League_Name

class Meeting(models.Model):
    meeting_ID = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular meet')
    League = models.ForeignKey('League', on_delete=models.SET_NULL, null=True)
    Season = models.ForeignKey('Season', on_delete=models.SET_NULL, null=True)
    meeting_name = models.CharField(max_length=40)
    meeting_date = models.DateField(null=True, blank=True)


    def __str__(self):
        return self.meeting_name

    def get_absolute_url(self):
        """Returns the url to access a detail record for this athlete."""
        return reverse('meeting-detail', args=[str(self.meeting_ID)])

class Venue(models.Model):
    Venue_ID = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular Venue')
    Venue_name = models.CharField(max_length=40)
    Venue_location = models.CharField(max_length=40)

    def __str__(self):
        return self.Venue_name
    
    COMP_COUNTY = (
        ('Su', 'Surrey'),
        ('We', 'Wessex'),
        ('Sus', 'Sussex'),
        ('Ke', 'Kent'),
        ('Es','Essex')
    )

    status = models.CharField(
        max_length=10000000,
        choices=COMP_COUNTY,
        blank=True,
        default='Su',
        help_text='county',
    )

def get_absolute_url(self):
        """Returns the url to access a detail record for this athlete."""
        return reverse('venue-detail', args=[str(self.Venue_ID)])
    
class Event(models.Model):
    event_ID = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular event')
    Meeting = models.ForeignKey('Meeting', on_delete=models.SET_NULL, null=True)
    Speciality = models.ForeignKey('Speciality', on_delete=models.SET_NULL, null=True);
    round_type = models.ForeignKey('EventRound', on_delete=models.SET_NULL, null=True);
    event_name = models.CharField(max_length=40, null=True, blank=True)
    event_time = models.TimeField(null=True, blank=True)
    
    def __str__(self):
        return self.Meeting.meeting_name + ' - ' + self.Speciality.speciality_name + ' - ' + self.event_name

    def get_absolute_url(self):
        """Returns the url to access a detail record for this event."""
        return reverse('event-detail', args=[str(self.event_ID)])

class EventRound(models.Model):
    eventRound_ID = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular event round')
    round_type = (
        ('Heat', 'Heat'),
        ('Semi-final', 'Semi-final'),
        ('Final', 'Final')
    )

    event_round = models.CharField(
        max_length=10000000,
        choices=round_type,
        blank=True,
        default='Heat',
        help_text='Round Type',

    )

    def __str__(self):
        return self.event_round

class EventParticipant(models.Model):
    eventParticipant_ID = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular event participant')
    Event = models.ForeignKey('Event', on_delete=models.SET_NULL, null=True)
    Athlete = models.ForeignKey('Athlete', on_delete=models.SET_NULL, null=True)
    bib = models.CharField(max_length=3)
    lane = models.PositiveIntegerField(default=1,validators=[MinValueValidator(1), MaxValueValidator(100)],null=True, blank=True)
   
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['Event', 'Athlete'], name='unique athlete for event'),
            models.UniqueConstraint(fields=['Event','bib'], name='unique bib for event')
        ]

    def __str__(self):
        return self.Event.Meeting.meeting_name + ' - ' + self.Event.Speciality.speciality_name + ' - ' + str(self.lane) + ' - ' + self.Athlete.Athlete_Surname + ' - ' + self.bib

    def get_absolute_url(self):
        """Returns the url to access a detail record for this athlete."""
        return reverse('event-participant-detail', args=[str(self.eventParticipant_ID)])

class TrackEventResult(models.Model):
    TrackEventResult_ID = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular track event result')
    EventParticipant = models.ForeignKey('EventParticipant', on_delete=models.SET_NULL, null=True)
    duration = models.DurationField(null=False, blank=False)

    def __str__(self):
        return self.EventParticipant.Event.Meeting.meeting_name + ' - ' + self.EventParticipant.Event.Speciality.speciality_name + ' - ' + str(self.EventParticipant.lane) + ' - ' + self.EventParticipant.Athlete.Athlete_Surname + ' - ' + self.EventParticipant.bib + ' - ' + str(self.duration)

    def get_absolute_url(self):
        """Returns the url to access a detail record for this athlete."""
        return reverse('track-event-result-detail', args=[str(self.TrackEventResult_ID)])


class FieldEventResult(models.Model):
    FieldEventResult_ID = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular field event result')
    EventParticipant = models.ForeignKey('EventParticipant', on_delete=models.SET_NULL, null=True)
    distance = models.DecimalField(max_digits=20, decimal_places=1)

  
    def __str__(self):
        return self.EventParticipant.Event.Meeting.meeting_name + ' - ' + self.EventParticipant.Event.event_name + ' - ' + str(self.EventParticipant.lane) + ' - ' + self.EventParticipant.Athlete.Athlete_Surname + ' - ' + self.EventParticipant.bib

    def get_absolute_url(self):
        """Returns the url to access a detail record for this athlete."""
        return reverse('field-event-result-detail', args=[str(self.FieldEventResult_ID)])


class Season(models.Model):
    season_ID = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular season')
    season_Name = models.CharField(max_length=20)
    SEASON_YEAR = (
        ('15/16', '2015/2016'),
        ('16/17', '2016/2017'),
        ('17/18', '2017/2018'),
        ('18/19', '2018/2019'),
        ('19/20', '2019/2020'),
        ('20/21', '2020/2021'),
        ('21/22', '2021/2022'),
        ('ALL', 'ALL'),
    )

    season_year = models.CharField(
        max_length=10000000,
        choices=SEASON_YEAR,
        blank=True,
        default='15/16',
        help_text='Season',
    )

    def __str__(self):
        return self.season_Name

    def get_absolute_url(self):
        return reverse('season-detail', args=[str(self.season_ID)])

