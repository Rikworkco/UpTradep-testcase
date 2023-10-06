from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_menu_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='code_name',
            field=models.TextField(default='menu'),
        ),
    ]