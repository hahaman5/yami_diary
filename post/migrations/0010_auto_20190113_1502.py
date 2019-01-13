# Generated by Django 2.1.5 on 2019-01-13 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0009_auto_20190105_2258'),
    ]

    operations = [
        migrations.AddField(
            model_name='idea',
            name='memo',
            field=models.TextField(blank=True, max_length=500, verbose_name='메모'),
        ),
        migrations.AlterField(
            model_name='division',
            name='division',
            field=models.CharField(max_length=100, primary_key=True, serialize=False, verbose_name='분류'),
        ),
    ]
