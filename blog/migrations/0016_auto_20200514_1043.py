# Generated by Django 3.0.4 on 2020-05-14 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Numéro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=100)),
                ('num', models.CharField(max_length=20)),
                ('description', models.TextField(blank=True, max_length=250, null=True)),
            ],
            options={
                'verbose_name': 'numero',
                'ordering': ['titre'],
            },
        ),
        migrations.AddField(
            model_name='contact',
            name='description',
            field=models.TextField(blank=True, max_length=250, null=True),
        ),
    ]
