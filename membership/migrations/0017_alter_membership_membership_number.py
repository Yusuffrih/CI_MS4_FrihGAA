# Generated by Django 3.2.9 on 2021-12-10 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0016_alter_membership_membership_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='membership_number',
            field=models.UUIDField(default='0E3A31BF', editable=False, unique=True),
        ),
    ]
