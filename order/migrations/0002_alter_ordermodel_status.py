# Generated by Django 5.1.2 on 2025-02-22 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='status',
            field=models.IntegerField(choices=[(1, 'Pending Payment'), (2, 'Successful'), (3, 'Canceled')], default=1),
        ),
    ]
