# Generated by Django 3.0.6 on 2020-07-31 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question_Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='videos/')),
                ('publication', models.CharField(max_length=50)),
                ('std', models.IntegerField()),
                ('chapter', models.IntegerField()),
                ('Question_no', models.IntegerField()),
                ('Question', models.CharField(max_length=500)),
            ],
        ),
    ]
