# Generated by Django 4.2 on 2023-06-27 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200, verbose_name='text')),
                ('answer_a', models.CharField(max_length=50, verbose_name='answer A')),
                ('answer_b', models.CharField(max_length=50, verbose_name='answer B')),
                ('answer_c', models.CharField(max_length=50, verbose_name='answer C')),
                ('answer_d', models.CharField(max_length=50, verbose_name='answer D')),
                ('correct_answer', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=1, verbose_name='correct answer')),
                ('is_correct', models.BooleanField(default=False, verbose_name='is correct')),
            ],
        ),
    ]