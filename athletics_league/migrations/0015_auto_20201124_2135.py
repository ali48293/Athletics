# Generated by Django 3.0.8 on 2020-11-24 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('athletics_league', '0014_auto_20201124_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trackeventresult',
            name='EventParticipant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='athletics_league.EventParticipant'),
        ),
    ]
