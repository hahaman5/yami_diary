# Generated by Django 2.1.5 on 2019-01-05 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0007_auto_20190105_1826'),
    ]

    operations = [
        migrations.CreateModel(
            name='Division',
            fields=[
                ('division', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.AlterField(
            model_name='idea',
            name='division',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.Division'),
        ),
    ]