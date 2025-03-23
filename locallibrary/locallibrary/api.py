from ninja import NinjaAPI, Schema
from ninja.pagination import paginate
from typing import List, Optional
from datetime import date
from catalog.models import Author, Genre, Language
from django.shortcuts import get_object_or_404

api = NinjaAPI()

# Schemas for Author
class AuthorIn(Schema):
    first_name: str
    last_name: str
    date_of_birth: Optional[date] = None
    date_of_death: Optional[date] = None

class AuthorOut(Schema):
    id: int
    first_name: str
    last_name: str
    date_of_birth: Optional[date] = None
    date_of_death: Optional[date] = None

# Schemas for Genre
class GenreIn(Schema):
    name: str

class GenreOut(Schema):
    id: int
    name: str

# Schemas for Language
class LanguageIn(Schema):
    name: str

class LanguageOut(Schema):
    id: int
    name: str

# Author CRUD endpoints
@api.get("/authors", response=List[AuthorOut])
@paginate
def list_authors(request):
    return Author.objects.all()

@api.get("/authors/{author_id}", response=AuthorOut)
def get_author(request, author_id: int):
    return get_object_or_404(Author, id=author_id)

@api.post("/authors", response=AuthorOut)
def create_author(request, payload: AuthorIn):
    author = Author.objects.create(**payload.dict())
    return author

@api.put("/authors/{author_id}", response=AuthorOut)
def update_author(request, author_id: int, payload: AuthorIn):
    author = get_object_or_404(Author, id=author_id)
    for attr, value in payload.dict().items():
        setattr(author, attr, value)
    author.save()
    return author

@api.delete("/authors/{author_id}")
def delete_author(request, author_id: int):
    author = get_object_or_404(Author, id=author_id)
    author.delete()
    return {"success": True}

# Genre CRUD endpoints
@api.get("/genres", response=List[GenreOut])
@paginate
def list_genres(request):
    return Genre.objects.all()

@api.get("/genres/{genre_id}", response=GenreOut)
def get_genre(request, genre_id: int):
    return get_object_or_404(Genre, id=genre_id)

@api.post("/genres", response=GenreOut)
def create_genre(request, payload: GenreIn):
    genre = Genre.objects.create(**payload.dict())
    return genre

@api.put("/genres/{genre_id}", response=GenreOut)
def update_genre(request, genre_id: int, payload: GenreIn):
    genre = get_object_or_404(Genre, id=genre_id)
    for attr, value in payload.dict().items():
        setattr(genre, attr, value)
    genre.save()
    return genre

@api.delete("/genres/{genre_id}")
def delete_genre(request, genre_id: int):
    genre = get_object_or_404(Genre, id=genre_id)
    genre.delete()
    return {"success": True}

# Language CRUD endpoints
@api.get("/languages", response=List[LanguageOut])
@paginate
def list_languages(request):
    return Language.objects.all()

@api.get("/languages/{language_id}", response=LanguageOut)
def get_language(request, language_id: int):
    return get_object_or_404(Language, id=language_id)

@api.post("/languages", response=LanguageOut)
def create_language(request, payload: LanguageIn):
    language = Language.objects.create(**payload.dict())
    return language

@api.put("/languages/{language_id}", response=LanguageOut)
def update_language(request, language_id: int, payload: LanguageIn):
    language = get_object_or_404(Language, id=language_id)
    for attr, value in payload.dict().items():
        setattr(language, attr, value)
    language.save()
    return language

@api.delete("/languages/{language_id}")
def delete_language(request, language_id: int):
    language = get_object_or_404(Language, id=language_id)
    language.delete()
    return {"success": True}