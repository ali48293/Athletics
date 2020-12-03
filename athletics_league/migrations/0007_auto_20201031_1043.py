# Generated by Django 2.2.12 on 2020-10-31 10:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('athletics_league', '0006_auto_20201031_1038'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='speciality',
            name='status',
        ),
        migrations.AddField(
            model_name='athletepb',
            name='Speciality_Type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='athletics_league.SpecialityType'),
        ),
    ]