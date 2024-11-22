from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from core.models import Colecao, Livro, Categoria, Autor

class ColecaoTests(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser(username='adm', password='adminpass')
        self.user_rafa = User.objects.create_user(username='rafa', password='password')
        self.user_ana = User.objects.create_user(username='ana', password='password')

        self.token_rafa = Token.objects.create(user=self.user_rafa)
        self.token_ana = Token.objects.create(user=self.user_ana)

        self.categoria = Categoria.objects.create(nome="Ficção Científica")
        self.autor = Autor.objects.create(nome="Autor Teste")

        self.livro = Livro.objects.create(
            titulo='Livro de Teste',
            autor=self.autor,
            categoria=self.categoria,
            publicado_em='2024-01-01'
        )

        self.colecao = Colecao.objects.create(
            nome="Coleção Teste",
            colecionador=self.user_rafa
        )
        self.colecao.livros.set([self.livro])

    def test_create_colecao_authenticated(self):
       
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token_rafa.key)

        data = {
            'nome': 'Nova Coleção',
            'colecionador': self.user_rafa.id, 
        }
        
        response = self.client.post('/api/colecoes/', data, format='json')
        
        self.assertEqual(response.status_code, 201)

    def test_create_colecao_unauthenticated(self):
        
        data = {'nome': 'Nova Coleção'}
        response = self.client.post('/api/colecoes/', data, format='json')
        
        self.assertEqual(response.status_code, 401)

    def test_delete_colecao_by_own_user(self):
        
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token_rafa.key)
        
        response = self.client.delete(f'/api/colecoes/{self.colecao.id}/')
        
        self.assertEqual(response.status_code, 204)

    def test_delete_colecao_by_other_user(self):
      
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token_ana.key)
        
        response = self.client.delete(f'/api/colecoes/{self.colecao.id}/')
        
        self.assertEqual(response.status_code, 403)


    def test_edit_colecao_by_other_user(self):
      
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token_ana.key)

        livro = Livro.objects.create(
            titulo='Livro de Teste',
            autor=self.autor,  
            categoria=self.categoria,  
            publicado_em='2024-01-01'
        )
        self.colecao.livros.add(livro)

        data = {
            'nome': 'Coleção Editada',
            'livros': [livro.id]
         }

        response = self.client.put(f'/api/colecoes/{self.colecao.id}/', data, format='json')

        self.assertEqual(response.status_code, 403)

    """"
    def test_list_colecoes_authenticated(self):
            
            self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token_rafa.key)
            response = self.client.get('/api/colecoes/')
            self.assertEqual(response.status_code, 200)
            colecoes = response.json()
            print("Response data:", colecoes)  
            self.assertTrue(len(colecoes) > 0)
            self.assertEqual(colecoes[0]['colecionador'], self.user_rafa.username) 
    """