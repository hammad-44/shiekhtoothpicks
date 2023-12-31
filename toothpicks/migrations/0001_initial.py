# Generated by Django 4.2.2 on 2023-10-10 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacst',
            fields=[
                ('sno', models.AutoField(default=1, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('message', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('number', models.CharField(max_length=255)),
                ('product', models.CharField(max_length=55)),
                ('quantity', models.CharField(max_length=55)),
                ('message', models.TextField(max_length=255)),
                ('date', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('desc', models.CharField(max_length=255)),
                ('price', models.CharField(max_length=30)),
                ('img', models.ImageField(upload_to='static/products/')),
            ],
        ),
    ]
