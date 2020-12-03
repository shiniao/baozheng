# Generated by Django 3.1.4 on 2020-12-03 07:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mark', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='source',
            name='category',
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.CharField(max_length=200)),
                ('choice', models.BooleanField()),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mark.source')),
            ],
        ),
    ]
