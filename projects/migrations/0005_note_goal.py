# Generated by Django 4.2.11 on 2024-03-28 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_rename_comletion_percentage_goal_completion_percentage'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='goal',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='projects.goal'),
            preserve_default=False,
        ),
    ]