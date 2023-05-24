# Generated by Django 4.2.1 on 2023-05-24 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
        ('users', '0003_alter_user_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='organization',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='staff.organization', verbose_name='Организация'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='citizenship',
            field=models.CharField(blank=True, max_length=50, verbose_name='Гражданство'),
        ),
    ]