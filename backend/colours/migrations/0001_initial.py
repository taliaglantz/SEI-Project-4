# Generated by Django 3.2.9 on 2021-12-03 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Colour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Black', 'Black'), ('Yellow', 'Yellow'), ('Blue', 'Blue'), ('Red', 'Red'), ('Green', 'Green'), ('Orange', 'Orange'), ('White', 'White'), ('Purple', 'Purple'), ('Brown', 'Brown'), ('Grey', 'Grey'), ('Beige', 'Beige'), ('Pink', 'Pink')], default=None, max_length=100)),
            ],
        ),
    ]
