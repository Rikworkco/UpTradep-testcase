from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_menu_code_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menu',
            old_name='code_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='title',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='url',
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(default='Меню')),
                ('url', models.TextField(default='/')),
                ('children', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.menu')),
            ],
        ),
        migrations.AddField(
            model_name='menu',
            name='menu_items',
            field=models.ManyToManyField(to='backend.menuitem'),
        ),
    ]
