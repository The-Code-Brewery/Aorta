# Generated by Django 2.2.5 on 2019-09-14 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_auto_20190914_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='phonenumber',
            field=models.CharField(blank=True, default=None, max_length=10),
        ),
    ]
