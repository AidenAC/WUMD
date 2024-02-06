# Generated by Django 4.2.9 on 2024-02-06 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pages', '0002_member_show_eboard'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='day',
            field=models.CharField(max_length=10, null=True, verbose_name='Day on Air'),
        ),
        migrations.AddField(
            model_name='show',
            name='time',
            field=models.TimeField(null=True, verbose_name='Air Time'),
        ),
    ]