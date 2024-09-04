from django.test import TestCase
from django.test import Client
from django.urls import reverse_lazy
from ..views import IndexView
from random import randint

class IndexViewTestCase(TestCase):

    def setUp(self):
        self.dados = {
            'nome': 'alan',
            'email': 'alan@python.com',
            'assunto': 'teste assunto',
            'mensagem': 'teste mensagem]',
        }
        
        self.cliente = Client()

    def test_form_valid(self):
        request = self.cliente.post(reverse_lazy('index'), data=self.dados)
        self.assertEquals(request.status_code, 302)

    def test_form_invalid(self):
        self.dados['nome'] = ''
        request = self.client.post(reverse_lazy('index'), data=self.dados)
        self.assertEquals(request.status_code, 200)

    def test_get_feature_half_index(self):
        view = IndexView()        
        half_index = view.get_feature_half_index(total_features=4)
        self.assertEqual(half_index, 2)

        half_index = view.get_feature_half_index(total_features=8)
        self.assertEqual(half_index, 4)

        half_index = view.get_feature_half_index(total_features=12)
        self.assertEqual(half_index, 6)