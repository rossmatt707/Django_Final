# Generated by Django 5.1.1 on 2024-09-12 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Checkbook', '0003_alter_account_managers_alter_transaction_managers'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='account',
            managers=[
            ],
        ),
        migrations.AlterModelManagers(
            name='transaction',
            managers=[
            ],
        ),
    ]