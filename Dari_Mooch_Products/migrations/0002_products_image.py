# Generated by Django 5.0.6 on 2024-06-25 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dari_Mooch_Products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='image',
            field=models.FileField(max_length=200, null=True, upload_to='products/'),
        ),
    ]