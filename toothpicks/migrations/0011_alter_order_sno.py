# Generated by Django 4.2.2 on 2023-06-25 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toothpicks', '0010_remove_contact_id_remove_order_id_contact_sno_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='sno',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
