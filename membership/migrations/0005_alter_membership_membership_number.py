# Generated by Django 3.2.9 on 2021-11-14 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0004_alter_membership_membership_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='membership_number',
            field=models.UUIDField(default='B539F897E53348C3B450F574C15C09A0', editable=False, unique=True),
        ),
    ]
