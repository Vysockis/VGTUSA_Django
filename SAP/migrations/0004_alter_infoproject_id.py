# Generated by Django 4.0.1 on 2022-02-10 20:50

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('SAP', '0003_delete_auth_user_infoproject_moderators'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infoproject',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
