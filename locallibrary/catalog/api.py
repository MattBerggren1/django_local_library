from ninja import NinjaAPI
from typing import List
from django.shortcuts import get_object_or_404
from catalog.models import Author, Genre, Language
from ninja.orm import create_schema

api = NinjaAPI()

AuthorSchema = create_schema(Author) # FIXME: prefer https://django-ninja.dev/guides/response/django-pydantic/#modelschema to create_schema for most cases
GenreSchema = create_schema(Genre)
LanguageSchema = create_schema(Language)

# Author endpoints
@api.get("/authors", response=List[AuthorSchema])
def list_authors(request):
    return Author.objects.all()

@api.get("/authors/{author_id}", response=AuthorSchema)
def get_author(request, author_id: int):
    return get_object_or_404(Author, id=author_id)

@api.post("/authors", response=AuthorSchema)
def create_author(request, data: AuthorSchema):
    author = Author.objects.create(**data.dict())
    return author

@api.put("/authors/{author_id}", response=AuthorSchema)
def update_author(request, author_id: int, data: AuthorSchema):
    author = get_object_or_404(Author, id=author_id)
    for attr, value in data.dict().items():
        setattr(author, attr, value)
    author.save()
    return author

@api.delete("/authors/{author_id}", response={204: None})
def delete_author(request, author_id: int):
    author = get_object_or_404(Author, id=author_id)
    author.delete()
    return 204, None

# Genre endpoints
@api.get("/genres", response=List[GenreSchema])
def list_genres(request):
    return Genre.objects.all()

@api.get("/genres/{genre_id}", response=GenreSchema)
def get_genre(request, genre_id: int):
    return get_object_or_404(Genre, id=genre_id)

@api.post("/genres", response=GenreSchema)
def create_genre(request, data: GenreSchema):
    genre = Genre.objects.create(**data.dict())
    return genre

@api.put("/genres/{genre_id}", response=GenreSchema)
def update_genre(request, genre_id: int, data: GenreSchema):
    genre = get_object_or_404(Genre, id=genre_id)
    for attr, value in data.dict().items():
        setattr(genre, attr, value)
    genre.save()
    return genre

@api.delete("/genres/{genre_id}", response={204: None})
def delete_genre(request, genre_id: int):
    genre = get_object_or_404(Genre, id=genre_id)
    genre.delete()
    return 204, None

# Language endpoints
@api.get("/languages", response=List[LanguageSchema])
def list_languages(request):
    return Language.objects.all()

@api.get("/languages/{language_id}", response=LanguageSchema)
def get_language(request, language_id: int):
    return get_object_or_404(Language, id=language_id)

@api.post("/languages", response=LanguageSchema)
def create_language(request, data: LanguageSchema):
    language = Language.objects.create(**data.dict())
    return language

@api.put("/languages/{language_id}", response=LanguageSchema)
def update_language(request, language_id: int, data: LanguageSchema):
    language = get_object_or_404(Language, id=language_id)
    for attr, value in data.dict().items():
        setattr(language, attr, value)
    language.save()
    return language

@api.delete("/languages/{language_id}", response={204: None})
def delete_language(request, language_id: int):
    language = get_object_or_404(Language, id=language_id)
    language.delete()
    return 204, None