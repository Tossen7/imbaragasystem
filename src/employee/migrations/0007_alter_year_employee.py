# Generated by Django 3.2.4 on 2021-07-28 10:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0006_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='year',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.employee', verbose_name='Employee'),
        ),
    ]
