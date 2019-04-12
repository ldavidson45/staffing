# Generated by Django 2.2 on 2019-04-11 20:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('staffing', '0006_auto_20190409_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role_log',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='role_logs', to='staffing.Employee'),
        ),
        migrations.AlterField(
            model_name='role_log',
            name='role_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='role_logs', to='staffing.Role_Type'),
        ),
    ]
