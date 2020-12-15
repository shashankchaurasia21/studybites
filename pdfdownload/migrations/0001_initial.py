# Generated by Django 3.0.3 on 2020-04-19 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pdftute',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('subtitle', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('slug', models.CharField(max_length=130)),
                ('upload', models.FileField(upload_to='media/file/')),
                ('timeStamp', models.DateTimeField(blank=True)),
            ],
        ),
    ]
