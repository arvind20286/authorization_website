# Generated by Django 4.2.15 on 2024-09-12 19:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthProvider',
            fields=[
                ('name', models.CharField(max_length=10, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('password', models.CharField(blank=True, max_length=20, null=True)),
                ('google_id', models.CharField(blank=True, max_length=255, null=True)),
                ('auth_provider', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth_app.authprovider')),
            ],
        ),
    ]
