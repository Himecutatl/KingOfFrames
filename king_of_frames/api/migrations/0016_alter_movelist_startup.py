# Generated by Django 4.1.1 on 2022-09-14 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_alter_movelist_stun'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movelist',
            name='startup',
            field=models.CharField(default=None, max_length=5, null=True, verbose_name='startup'),
        ),
    ]