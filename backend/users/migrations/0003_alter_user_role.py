# Generated by Django 4.2.1 on 2023-05-24 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_userinfo_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('CANDIDATE', 'Кандидат'), ('INTERN', 'Стажер'), ('CURATOR', 'Куратор'), ('STAFF', 'Кадровый специалист'), ('MENTOR', 'Наставник')], db_index=True, default='CANDIDATE', max_length=16, verbose_name='Роль'),
        ),
    ]
