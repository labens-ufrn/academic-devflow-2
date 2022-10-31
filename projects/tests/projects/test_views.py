from django.test import TestCase,Client
from django.urls import reverse_lazy,reverse
from projects.models import Projeto
from projects.views import update_view, get_All_Projects

class ProjetoUpdateView(TestCase):
    DESCRICAO = 'Teste do modelo projeto'
    DT_INICIO = '2010-10-10'
    DT_TERMINO = '2011-11-11'
    NOME = 'Teste'
    SITUACAO = 'Em desenvolvimento'

    def setUp(self):
        self.PROJETO_OBJ = Projeto.objects.create(descricao=self.DESCRICAO, dt_inicio=self.DT_INICIO,
                                                  dt_termino=self.DT_TERMINO, nome=self.NOME, situacao=self.SITUACAO)

    def test_nome_do_projeto_editavel(self):
        """Testa se o campo 'nome' de um objeto Projeto é editável"""

        novo_nome = "nome 2"
        url = reverse_lazy('projects:update', args=[self.PROJETO_OBJ.id])
        data = {
            "descricao": self.PROJETO_OBJ.descricao,
            "dt_inicio": self.PROJETO_OBJ.dt_inicio,
            "dt_termino": self.PROJETO_OBJ.dt_termino,
            "nome": novo_nome,
            "situacao": self.PROJETO_OBJ.situacao
        }
        self.client.post(url, data)

        projeto_atualizado = Projeto.objects.filter(nome=novo_nome).first()
        self.assertIsNotNone(projeto_atualizado)

class ProjetoGetAllProjets(TestCase):

    def test_get_All_Projects(self):
        client = Client()
        response = client.get(reverse('get'))

        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'projects/index.html')