# Generated by Django 2.2.3 on 2019-11-13 03:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=50)),
                ('age', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('tamount', models.IntegerField(default=0)),
                ('quantity', models.IntegerField(default=0)),
                ('address', models.CharField(max_length=50)),
                ('date', models.CharField(max_length=20)),
                ('mail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.user')),
            ],
        ),
    ]
