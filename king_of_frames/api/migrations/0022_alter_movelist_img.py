# Generated by Django 4.1.1 on 2022-09-20 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_alter_movelist_damage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movelist',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
