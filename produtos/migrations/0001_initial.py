# Generated by Django 4.0.1 on 2022-01-18 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=200, null=True, verbose_name='Descrição')),
                ('custo', models.DecimalField(decimal_places=2, max_digits=7, null=True, verbose_name='Custo')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=7, null=True, verbose_name='Preço')),
                ('fornecedor', models.CharField(max_length=100, null=True, verbose_name='Fornecedor')),
                ('quantidade', models.SmallIntegerField(null=True, verbose_name='Quantidade')),
                ('peso', models.SmallIntegerField(null=True, verbose_name='Peso')),
            ],
        ),
    ]
