# Generated by Django 4.1.1 on 2022-09-14 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_alter_movelist_startup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movelist',
            name='startup',
            field=models.CharField(default=None, max_length=100, null=True, verbose_name='startup'),
        ),
    ]
