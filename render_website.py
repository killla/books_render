from jinja2 import Environment, FileSystemLoader, select_autoescape
from livereload import Server, shell
from more_itertools import chunked
from pathlib import Path
import json, os


env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)


def render_page(page_number, count_of_pages, books):
    template = env.get_template('page_template.html')
    books = list(chunked(books, 2))

    prev_url, next_url = None, None
    if page_number > 1:
        prev_url = f'./index{page_number-1}.html'
    if page_number < count_of_pages:
        next_url = f'./index{page_number+1}.html'

    rendered_page = template.render(
        books=books,
        prev_url=prev_url,
        next_url=next_url,
        page_number=page_number,
        count_of_pages=count_of_pages,
    )
    page_filename = os.path.join('pages', f'index{page_number}.html')

    with open(page_filename, 'w', encoding="utf8") as file:
        file.write(rendered_page)
    return page_filename


def delete_old_pages(paths):
    for filename in Path('.').glob('pages/index*.html'):
        if str(filename) not in paths:
            os.remove(filename)


def render_pages():
    book_on_page = 10

    with open("books.json", "r") as books_file:
        books_json = books_file.read()
    books = json.loads(books_json)
    books_by_pages = list(chunked(books, book_on_page))

    count_of_pages = len(books_by_pages)
    paths_of_pages = []

    for page_number, books_on_current_page in enumerate(books_by_pages, 1):
        page_path = render_page(page_number, count_of_pages, books_on_current_page)
        paths_of_pages.append(page_path)

    template = env.get_template('main_page_template.html')
    rendered_page = template.render(page_count = count_of_pages)
    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)
    delete_old_pages(paths_of_pages)


if __name__ =='__main__':
    render_pages()
    server = Server()
    server.watch('page_template.html', render_pages)
    server.serve(root='.')
