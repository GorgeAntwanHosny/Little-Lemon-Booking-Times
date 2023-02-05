# Generated by Django 4.1.4 on 2022-12-07 13:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('restaurant', '0002_menu_menu_item_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='guest_number',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='last_name',
        ),
        migrations.AddField(
            model_name='booking',
            name='reservation_date',
            field=models.DateField(default="2022-12-07"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='booking',
            name='reservation_slot',
            field=models.SmallIntegerField(default=10),
        ),
    ]
