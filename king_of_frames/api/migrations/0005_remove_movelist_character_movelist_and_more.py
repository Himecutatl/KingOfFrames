# Generated by Django 4.1.1 on 2022-09-07 22:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_character_thumbnail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movelist',
            name='character_movelist',
        ),
        migrations.AlterField(
            model_name='movelist',
            name='character_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='move_list', to='api.character'),
        ),
    ]
