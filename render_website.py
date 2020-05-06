from jinja2 import Environment, FileSystemLoader, select_autoescape
from livereload import Server, shell
from more_itertools import chunked
import json, math, os


env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)


def render_page(page_number, count_of_page, book_on_page, books):
    template = env.get_template('page_template.html')
    begin = book_on_page * (page_number - 1)
    end = book_on_page * page_number
    books = books[begin:end]
    books = list(chunked(books, 2))

    prev_url, next_url = None, None
    if page_number > 1:
        prev_url = f'./index{page_number-1}.html'
    if page_number < count_of_page:
        next_url = f'./index{page_number+1}.html'

    rendered_page = template.render(
        books=books,
        prev_url=prev_url,
        next_url=next_url,
        page_number=page_number,
    )
    page_filename = os.path.join('pages', f'index{page_number}.html')

    with open(page_filename, 'w', encoding="utf8") as file:
        file.write(rendered_page)


def render_pages():
    book_on_page = 10

    with open("books.json", "r") as books_file:
        books_json = books_file.read()
    books_list = json.loads(books_json)

    count_of_page = math.ceil(len(books_list)/book_on_page)

    for page_number in range(1, count_of_page+1):
        render_page(page_number, count_of_page, book_on_page, books_list)

    template = env.get_template('main_page_template.html')
    rendered_page = template.render(page_count = count_of_page)
    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)


if __name__ =='__main__':
    render_pages()
    server = Server()
    server.watch('page_template.html', render_pages)
    server.serve(root='.')
