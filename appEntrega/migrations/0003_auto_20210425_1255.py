# Generated by Django 3.2 on 2021-04-25 10:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appEntrega', '0002_auto_20210424_0014'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orden_Linea',
            fields=[
                ('linea_referencia', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('linea_descripcion', models.CharField(max_length=250)),
                ('linea_unidades', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('linea_linea_padre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appEntrega.orden_linea')),
            ],
        ),
        migrations.CreateModel(
            name='Orden_Pedido',
            fields=[
                ('pedido_referencia', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('pedido_fecha', models.DateField()),
                ('pedido_descripcion', models.CharField(max_length=250)),
                ('pedido_precio', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('pedido_curso', models.BooleanField(default=False)),
                ('pedido_lanzado', models.BooleanField(default=False)),
                ('pedido_finalizado', models.BooleanField(default=False)),
                ('pedido_cliente_cif', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appEntrega.cliente')),
            ],
        ),
        migrations.RenameField(
            model_name='componente',
            old_name='producto',
            new_name='componente_producto',
        ),
        migrations.RenameField(
            model_name='componente',
            old_name='producto_padre',
            new_name='componente_producto_padre',
        ),
        migrations.RenameField(
            model_name='componente',
            old_name='componente_cantidad',
            new_name='componente_unidades',
        ),
        migrations.AlterField(
            model_name='componente',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.DeleteModel(
            name='Pedido',
        ),
        migrations.AddField(
            model_name='orden_linea',
            name='linea_pedido_referencia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appEntrega.orden_pedido'),
        ),
        migrations.AddField(
            model_name='orden_linea',
            name='linea_producto_referencia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appEntrega.producto'),
        ),
    ]