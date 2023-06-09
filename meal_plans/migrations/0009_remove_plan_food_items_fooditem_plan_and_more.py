# Generated by Django 4.2 on 2023-06-23 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meal_plans', '0008_alter_fooditem_carbohydrates_alter_fooditem_fat_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plan',
            name='food_items',
        ),
        migrations.AddField(
            model_name='fooditem',
            name='plan',
            field=models.ManyToManyField(to='meal_plans.plan'),
        ),
        migrations.AlterField(
            model_name='fooditem',
            name='item',
            field=models.TextField(blank=True),
        ),
    ]
