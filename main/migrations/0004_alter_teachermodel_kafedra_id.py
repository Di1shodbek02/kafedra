# Generated by Django 5.1.6 on 2025-06-09 08:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_fanmodel_kafedra_alter_teachermodel_kafedra_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teachermodel',
            name='kafedra_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teachers', to='main.kafedramodel'),
        ),
    ]
