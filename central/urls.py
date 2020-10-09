from django.urls import path
from . import views

# Esta variável app_name é importante para auxiliar a referênciar as urls criadas.
app_name = 'blog'

urlpatterns = [
    # Devido a utilização da url genérica abaixo será aguardado uma url com requisição ao template post_list.html.
    path('', views.PostListView.as_view(), name='lista'),
    # Na url abaixo se está requisitando o post relacionado ao slug com base no título do post clicado.
    path('<slug:slug>/', views.PostDetailView.as_view(), name='detalhe')
]
