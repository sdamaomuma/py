# Generated by Django 2.0 on 2018-04-16 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doshow', '0002_dwmoneyflow_presentproptbl'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=64)),
            ],
        ),
    ]