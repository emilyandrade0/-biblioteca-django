from rest_framework import generics, permissions
from django_filters import rest_framework as filters
from .models import Livro, Categoria, Autor, Colecao
from .serializers import LivroSerializer, CategoriaSerializer, AutorSerializer, ColecaoSerializer
from .custom_permissions import IsOwnerOrReadOnly
from .permissions import IsOwnerPermission

# Filtros para o modelo Livro
class LivroFilter(filters.FilterSet):
    titulo = filters.CharFilter(lookup_expr='icontains')
    autor = filters.CharFilter(field_name='autor__nome', lookup_expr='icontains')
    categoria = filters.AllValuesFilter(field_name='categoria__nome')

    class Meta:
        model = Livro
        fields = ['titulo', 'autor', 'categoria']

# Views para Livro
class LivroList(generics.ListCreateAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    filterset_class = LivroFilter
    ordering_fields = ['titulo', 'autor', 'categoria', 'publicado_em']  
    search_fields = ['titulo', 'autor__nome', 'categoria__nome']  

class LivroDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer

# Views para Categoria
class CategoriaList(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    filterset_fields = ['nome'] 
    ordering_fields = ['nome']  

class CategoriaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

# Views para Autor
class AutorList(generics.ListCreateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    ordering_fields = ['nome']  

class AutorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

# Views para Colecao
class ColecaoListCreate(generics.ListCreateAPIView):
  
    queryset = Colecao.objects.all()
    serializer_class = ColecaoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(colecionador=self.request.user)

class ColecaoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Colecao.objects.all()
    serializer_class = ColecaoSerializer
    permission_classes = [IsOwnerPermission, permissions.IsAuthenticated]

