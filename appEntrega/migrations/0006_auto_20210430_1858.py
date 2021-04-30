# Generated by Django 3.2 on 2021-04-30 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appEntrega', '0005_auto_20210429_1649'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orden_pedido',
            name='pedido_curso',
        ),
        migrations.RemoveField(
            model_name='orden_pedido',
            name='pedido_finalizado',
        ),
        migrations.RemoveField(
            model_name='orden_pedido',
            name='pedido_lanzado',
        ),
        migrations.AlterField(
            model_name='factura',
            name='linea_unidades',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='orden_pedido',
            name='pedido_descripcion',
            field=models.TextField(max_length=250),
        ),
        migrations.AlterField(
            model_name='orden_pedido',
            name='pedido_fecha',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='producto_referencia',
            field=models.CharField(max_length=13, primary_key=True, serialize=False),
        ),
    ]
