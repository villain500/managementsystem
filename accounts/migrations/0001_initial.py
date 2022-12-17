# Generated by Django 4.1.2 on 2022-12-16 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200, null=True)),
                ('Phone', models.CharField(max_length=200, null=True)),
                ('Email', models.CharField(max_length=200, null=True)),
                ('Date_Created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
