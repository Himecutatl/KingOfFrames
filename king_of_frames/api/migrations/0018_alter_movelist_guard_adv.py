# Generated by Django 4.1.1 on 2022-09-14 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_alter_movelist_startup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movelist',
            name='guard_adv',
            field=models.CharField(max_length=100, null=True, verbose_name='guard advantage'),
        ),
    ]
