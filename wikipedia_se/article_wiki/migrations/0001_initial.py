# Generated by Django 3.0.3 on 2020-09-01 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('titre_wiki', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('titre', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='titre_wiki.Titre')),
                ('content', models.TextField(blank=True)),
                ('created_At', models.DateField(auto_now_add=True)),
            ],
        ),
    ]