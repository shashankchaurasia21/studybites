# Generated by Django 3.0.3 on 2020-05-18 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pdfenglish',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('author', models.CharField(max_length=100)),
                ('upload', models.FileField(upload_to='media/file/')),
                ('timeStamp', models.DateTimeField(blank=True)),
            ],
        ),
    ]
