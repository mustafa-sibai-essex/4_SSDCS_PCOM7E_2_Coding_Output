# Generated by Django 4.1.3 on 2022-11-15 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operatorview', '0008_alter_vulnurability_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vulnurability',
            name='Status',
            field=models.CharField(choices=[('Awaiting Approval', 'Awaiting approval'), ('Assigned', 'Assigned'), ('Rejected', 'Rejected'), ('Fixed', 'Fixed'), ('Escalated', 'Escalated')], default='Awaiting Approval', max_length=25),
        ),
    ]