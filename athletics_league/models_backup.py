from django.db import models
import uuid
# Create your models here.

class Athlete(models.Model):
    """what consists of"""
    Athlete_ID = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular Athlete across whole league')
    Club = models.ForeignKey('Club', on_delete=models.SET_NULL, null=True)
    Athlete_Name = models.CharField(max_length=20)
    Athlete_Surname = models.CharField(max_length=20)
    Athlete_email = models.EmailField

    def __str__(self):
        """ athlete full name"""
        return self.Athlete_Name + self.Athlete_Surname

    AGEGROUP_STATUS = (
        ('u13', 'under 13'),
        ('u15', 'under 15'),
        ('u17', 'under 17'),
        ('u20', 'under 20'),
    )
    """ possible age group options"""

    status = models.CharField(
        max_length=1,
        choices=AGEGROUP_STATUS,
        blank=True,
        default='u13',
        help_text='athlete age group',
    )

    GENDER_TYPE= (
        ('M', 'Male'),
        ('F', 'Felmale'),
    )
    """possible gender options"""
    gender= models.CharField(
        max_length=1,
        choices=GENDER_TYPE,
        blank=True,
        default='M',
        help_text='Athlete Gender',
    )


    def get_absolute_url(self):
        """Returns the url to access a detail record for this athlete."""
        return reverse('athlete-detail', args=[str(self.id)])

class Club(models.Model):
    Club_ID = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular Club across whole league')
    League = models.ForeignKey('League', on_delete=models.SET_NULL, null=True)
    Club_Name = models.CharField(max_length=40)

    def __str__(self):
        """club name"""
        return self.Club_Name
    
   

class League(models.Model):
    League_ID = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular league')
    League_Name = models.CharField(max_length=40)

    def __str__(self):
        return self.League_Name

class Meeting(models.Model):
    meeting_ID = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular meet')
    League = models.ForeignKey('League', on_delete=models.SET_NULL, null=True)
    meeting_date = models.DateField 
    meeting_name = models.CharField(max_length=40)

    def __str__(self):
        return self.meeting_name

    def __str__(self):
        return self.meeting_date

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
        max_length=1,
        choices=COMP_COUNTY,
        blank=True,
        default='Su',
        help_text='county',
    )


class Event(models.Model):
    event_ID = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular event')
    event_name = models.CharField(max_length=20)

    def __str__(self):
        return self.event_name

    EVENT_CLASS = (
        ('T', 'Track'),
        ('F', 'Field'),
    )

    status = models.CharField(
        max_length=1,
        choices=EVENT_CLASS,
        blank=True,
        default='T',
        help_text='athlete event type',
    )


class Event_Result(models.Model):
    Athlete = models.ForeignKey('Athlete', on_delete=models.SET_NULL, null=True)
    Event = models.ForeignKey('Event', on_delete=models.SET_NULL, null=True)
    event_result = models.CharField(max_length=40)


    
        


    
