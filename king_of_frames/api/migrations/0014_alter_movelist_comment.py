# Generated by Django 4.1.1 on 2022-09-14 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_movelist_character_id_movelist_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movelist',
            name='comment',
            field=models.CharField(blank=True, default=None, max_length=500, null=True, verbose_name='comment'),
        ),
    ]
