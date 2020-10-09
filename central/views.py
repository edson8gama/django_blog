from django.views.generic import DetailView, ListView
from .models import Post

# Create your views here.


class PostListView(ListView):
    # Esta variável model já faz parte da super classe ListView. Esta classe tentará devolver o caminho para um
    # - template denominado automaticamente como post_list.html, então este template precisa ser criado fisicamente. E
    # - também retornará uma variável denominada post_list para ser utilizada no template criado.
    model = Post


class PostDetailView(DetailView):
    # Esta variável model já faz parte da super classe DetailView. Assim como a classe acima nesta classe também é
    # - criado um nome de template, denominado post_detail.html e há um retorno para este template, mas diferente da
    # - classe acima que retorna um objeto com todos os posts, aqui nesta classe é retornado apenas o post de acordo com
    # - o link clicado, devido ao slug relacionado. Analisar bem o arquivo urls.py
    model = Post
