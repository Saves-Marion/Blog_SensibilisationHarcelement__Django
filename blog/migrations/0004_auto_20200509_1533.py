# Generated by Django 3.0.4 on 2020-05-09 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_temoignages_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temoignages',
            name='resume',
            field=models.CharField(default='mon harcèlement', max_length=100),
        ),
    ]
