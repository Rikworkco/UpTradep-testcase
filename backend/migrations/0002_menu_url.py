from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='url',
            field=models.TextField(default='/'),
        ),
    ]
