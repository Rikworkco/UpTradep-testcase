from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_remove_menuitem_children_menuitem_children'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitem',
            name='children',
        ),
        migrations.AddField(
            model_name='menuitem',
            name='parents',
            field=models.ManyToManyField(blank=True, to='backend.menuitem'),
        ),
    ]
