from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_rename_code_name_menu_name_remove_menu_parent_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitem',
            name='children',
        ),
        migrations.AddField(
            model_name='menuitem',
            name='children',
            field=models.ManyToManyField(blank=True, null=True, to='backend.menuitem'),
        ),
    ]
