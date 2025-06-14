# Generated by Django 5.1.6 on 2025-06-09 08:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KafedraModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='QushimchalarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TarkibTuriModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('izoh', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='FanModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('talim_yunalishi', models.CharField(max_length=100)),
                ('kafedra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.kafedramodel')),
            ],
        ),
        migrations.CreateModel(
            name='KafedraFanModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fan_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.fanmodel')),
                ('kafedra_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.kafedramodel')),
                ('teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.qushimchalarmodel')),
            ],
        ),
        migrations.CreateModel(
            name='FanQushimchaModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('asos_nomi', models.CharField(max_length=100)),
                ('asos_file', models.FileField(upload_to='pics')),
                ('fan_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.fanmodel')),
                ('fan_qushimcha_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.qushimchalarmodel')),
            ],
        ),
        migrations.CreateModel(
            name='TeacherModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('kafedra_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.kafedramodel')),
            ],
        ),
    ]
