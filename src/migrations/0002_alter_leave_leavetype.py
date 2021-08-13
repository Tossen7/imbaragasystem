from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('leave', '0002_alter_leave_leavetype'),
    ]

    operations = [migrations.AlterField(
        model_name='leave',
        name = 'leavetype',
        field=models.CharField(choices=[('annual', 'Sick Leave'), ('circumstancial', 'Casual Leave')], default='annual', max_length=25, null=True),
        ),
    ]