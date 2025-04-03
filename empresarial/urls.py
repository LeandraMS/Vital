from django.urls import path
from . import views

urlpatterns = [
    path('gerenciar_clientes/', views.gerenciar_clientes, name="gerenciar_clientes"),
    path('cliente/<int:cliente_id>', views.cliente, name="cliente"),
    path('exame_cliente/<int:exame_id>', views.exame_cliente, name="exame_cliente"),
    path('proxy_pdf/<int:exame_id>', views.proxy_pdf, name="proxy_pdf"),
    path('gerar_senha/<int:exame_id>', views.gerar_senha, name="gerar_senha"),
    path('alterar_dados_exame/<int:exame_id>', views.alterar_dados_exame, name="alterar_dados_exame"),
]