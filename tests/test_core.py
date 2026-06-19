import pytest
from media_library import Book, Movie
from media_library.core import Media

def test_normal_media_summary():
    media = Media("인셉션", "놀란", 2010)
    assert media.get_summary() == "인셉션 (놀란, 2010)"

def test_normal_book_archive_score():
    book = Book("대하소설", "작가", 2020, 600)
    assert book.calculate_archive_score(2026) == 100

def test_normal_movie_archive_score():
    movie = Movie("장편영화", "감독", 2016, 130)
    assert movie.calculate_archive_score(2026) == 95

def test_normal_subclass_type_strings():
    book = Book("책", "저자", 2022, 200)
    movie = Movie("영화", "감독", 2024, 110)
    assert book.get_media_type() == "도서"
    assert movie.get_media_type() == "영화"

def test_normal_private_method_behavior():
    media = Media("Test Title", "Author", 2026)
    assert media._generate_base_id() == "MED-TES-2026"

def test_edge_empty_initialization():
    with pytest.raises(ValueError):
        Media("", "제작자", 2026)

def test_edge_invalid_future_year():
    media = Media("미래작품", "감독", 2026)
    with pytest.raises(ValueError):
        media.calculate_archive_score(2020)

def test_edge_book_negative_pages():
    with pytest.raises(ValueError):
        Book("오류도서", "저자", 2025, 0)

def test_edge_movie_negative_running_time():
    with pytest.raises(ValueError):
        Movie("오류영화", "감독", 2025, -120)