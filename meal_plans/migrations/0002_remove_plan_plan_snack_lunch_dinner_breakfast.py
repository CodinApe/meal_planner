# Generated by Django 4.2 on 2023-05-12 04:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meal_plans', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plan',
            name='plan',
        ),
        migrations.CreateModel(
            name='Snack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('snack', models.CharField(max_length=1000)),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meal_plans.plan')),
            ],
        ),
        migrations.CreateModel(
            name='Lunch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lunch', models.CharField(max_length=1000)),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meal_plans.plan')),
            ],
        ),
        migrations.CreateModel(
            name='Dinner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dinner', models.CharField(max_length=1000)),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meal_plans.plan')),
            ],
        ),
        migrations.CreateModel(
            name='Breakfast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('breakfast', models.CharField(max_length=1000)),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meal_plans.plan')),
            ],
        ),
    ]
