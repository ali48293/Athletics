# Generated by Django 3.0.8 on 2020-11-24 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('athletics_league', '0013_auto_20201114_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trackeventresult',
            name='EventParticipant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='athletics_league.EventParticipant'),
        ),
    ]