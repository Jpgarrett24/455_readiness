# Generated by Django 2.2.4 on 2020-06-26 22:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttributeType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_name', models.CharField(blank=True, max_length=255, null=True)),
                ('type', models.CharField(blank=True, max_length=255, null=True)),
                ('alert_type', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='attribute',
            name='alert_or_warning',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='attribute',
            name='attribute_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attribute', to='main.AttributeType'),
        ),
        migrations.AlterField(
            model_name='attribute',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='attribute',
            name='value',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='inputdata',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='inputdata',
            name='city',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='inputdata',
            name='civilian_email',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='inputdata',
            name='civilian_school',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='inputdata',
            name='employer',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='inputdata',
            name='location',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='inputdata',
            name='major',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='inputdata',
            name='military_schools',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='inputdata',
            name='num_credits',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='inputdata',
            name='phone_number',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='inputdata',
            name='plans_after',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='inputdata',
            name='state',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='inputdata',
            name='unit_destination',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='inputdata',
            name='unit_origin',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='inputdata',
            name='zipcode',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]
