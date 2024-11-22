from django.urls import path
from . import views
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    
    # schema OpenAPI
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    
    # documentação Swagger
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    
    # Rotas para Livro
    path('livros/', views.LivroList.as_view(), name='livros-list'),
    path('livros/<int:pk>/', views.LivroDetail.as_view(), name='livro-detail'),

    # Rotas para Categoria
    path('categorias/', views.CategoriaList.as_view(), name='categorias-list'),
    path('categorias/<int:pk>/', views.CategoriaDetail.as_view(), name='categoria-detail'),

    # Rotas para Autor
    path('autores/', views.AutorList.as_view(), name='autores-list'),
    path('autores/<int:pk>/', views.AutorDetail.as_view(), name='autor-detail'),

    # Rotas para Colecao
    path('colecoes/', views.ColecaoListCreate.as_view(), name='colecoes-list-create'),
    path('colecoes/<int:pk>/', views.ColecaoDetail.as_view(), name='colecoes-detail'),
]
