# Generated by Django 5.1.6 on 2025-06-09 08:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_fanmodel_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fanmodel',
            name='kafedra',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fanlar', to='main.kafedramodel'),
        ),
        migrations.AlterField(
            model_name='teachermodel',
            name='kafedra_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher', to='main.kafedramodel'),
        ),
    ]
