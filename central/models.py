from django.db import models as db
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class Post(db.Model):
    title = db.CharField(max_length=255)
    slug = db.SlugField(max_length=255, unique=True)
    # A tabela User tem o ID como chave primária, abaixo se está criando o campo author que será chave estrangeira do ID
    # - de User. Ao visualizar o campo ou coluna author no APP admin irá aparecer como author_id. A relação aqui é 1
    # - para muitos; pois um usuário pode escrever muitos posts. O parâmetro on_delete com argumento a partir do
    # - db.CASCADE indica que se o usuário é deletado, todos os posts criado por ele também serão deletados.
    author = db.ForeignKey(User, on_delete=db.CASCADE)
    body = db.TextField()
    created = db.DateTimeField(auto_now_add=True)
    updated = db.DateTimeField(auto_now=True)

    class Meta:
        # Com esta subclasse e a variável ordering se permite entregar os posts em uma determinada ordem com base em um
        # - campo. Como o argumento é -created se quer receber os posts a partir dos últimos acrescentados. Algo assim
        # - foi visto no projeto anterior mas a partir do módulo views, sem utilizar esta classe.
        ordering = ('-created',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # Com este método se pode criar os links dessa forma <a href="{{ post.get_absolute_url }}">{{ post.title }}</a>
        # - em vez de <a href="{% url 'blog:detalhe' post.slug %}">{{ post.title }}</a>. A vantagem é que se houver
        # - muitos templates que utilizem este metódo e é necessário alterar os links basta alterar aqui, no método, não
        # - em cada template.
        return reverse('blog:detalhe', kwargs={'slug': self.slug})
