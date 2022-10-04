# Generated by Django 4.1 on 2022-10-02 20:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Mixer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1024)),
                ('token', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('status', models.JSONField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MixerData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('p1_name', models.CharField(max_length=1024)),
                ('p1', models.FloatField(default=0)),
                ('p2_name', models.CharField(max_length=1024)),
                ('p2', models.FloatField(default=0)),
                ('p3_name', models.CharField(max_length=1024)),
                ('p3', models.FloatField(default=0)),
                ('p4_name', models.CharField(max_length=1024)),
                ('p4', models.FloatField(default=0)),
                ('p5_name', models.CharField(max_length=1024)),
                ('p5', models.FloatField(default=0)),
                ('p6_name', models.CharField(max_length=1024)),
                ('p6', models.FloatField(default=0)),
                ('p7_name', models.CharField(max_length=1024)),
                ('p7', models.FloatField(default=0)),
                ('p8_name', models.CharField(max_length=1024)),
                ('p8', models.FloatField(default=0)),
                ('mixer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mixer.mixer')),
            ],
        ),
    ]