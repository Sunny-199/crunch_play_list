# Generated by Django 4.0.5 on 2022-06-15 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crunchapp', '0003_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=10)),
            ],
        ),
    ]