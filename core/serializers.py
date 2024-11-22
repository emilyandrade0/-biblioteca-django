from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Categoria, Autor, Livro, Colecao

class CategoriaSerializer(serializers.Serializer): 
    id = serializers.IntegerField(read_only=True) 
    nome = serializers.CharField(max_length=100) 

    def create(self, validated_data): 
        return Categoria.objects.create(**validated_data) 

    def update(self, instance, validated_data): 
        instance.nome = validated_data.get('nome', instance.nome) 
        instance.save() 
        return instance 

class AutorSerializer(serializers.Serializer): 
    id = serializers.IntegerField(read_only=True) 
    nome = serializers.CharField(max_length=100) 

    def create(self, validated_data): 
        return Autor.objects.create(**validated_data)

    def update(self, instance, validated_data): 
        instance.nome = validated_data.get('nome', instance.nome) 
        instance.save() 
        return instance 

class LivroSerializer(serializers.Serializer): 
    id = serializers.IntegerField(read_only=True) 
    titulo = serializers.CharField(max_length=200) 
    autor = serializers.PrimaryKeyRelatedField(queryset=Autor.objects.all()) 
    categoria = serializers.PrimaryKeyRelatedField(queryset=Categoria.objects.all()) 
    publicado_em = serializers.DateField() 

    def create(self, validated_data): 
        return Livro.objects.create(**validated_data) 

    def update(self, instance, validated_data): 
        instance.titulo = validated_data.get('titulo', instance.titulo) 
        instance.autor = validated_data.get('autor', instance.autor) 
        instance.categoria = validated_data.get('categoria', instance.categoria) 
        instance.publicado_em = validated_data.get('publicado_em', instance.publicado_em) 
        instance.save() 
        return instance 

class ColecaoSerializer(serializers.ModelSerializer):
    livros = serializers.PrimaryKeyRelatedField(queryset=Livro.objects.all(), many=True, required=False)

    class Meta:
        model = Colecao
        fields = ['id', 'nome', 'colecionador', 'livros']

    def create(self, validated_data):
        livros_data = validated_data.pop('livros', [])
        colecao = Colecao.objects.create(**validated_data)
        colecao.livros.set(livros_data)  
        return colecao

    def update(self, instance, validated_data):
        livros_data = validated_data.pop('livros', [])
        instance.nome = validated_data.get('nome', instance.nome)
        instance.livros.set(livros_data) 
        instance.save()
        return instance
