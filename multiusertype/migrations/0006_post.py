# Generated by Django 4.0.5 on 2022-06-17 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multiusertype', '0005_alter_user_is_doctor_alter_user_is_patient'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=400)),
                ('body', models.TextField()),
                ('is_published', models.BooleanField(default=False)),
            ],
        ),
    ]
