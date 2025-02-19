# Generated by Django 5.0.3 on 2024-03-23 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('To Do', 'To Do'), ('In Progress', 'In Progress'), ('Done', 'Done')], default='To Do', max_length=100)),
                ('due_date', models.DateField()),
                ('slug', models.SlugField(max_length=250, null=True, unique=True)),
            ],
        ),
    ]
