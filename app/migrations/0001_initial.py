# Generated by Django 3.2.12 on 2022-03-24 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('phone_no', models.PositiveIntegerField()),
                ('instgram_handler', models.CharField(max_length=120)),
                ('email_address', models.EmailField(max_length=254, unique=True)),
                ('business_idea_craft_skill', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=200)),
            ],
        ),
    ]