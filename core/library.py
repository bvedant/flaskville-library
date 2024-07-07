from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from werkzeug.exceptions import abort

from core.auth import login_required
from core.db import get_db

bp = Blueprint('library', __name__)


@bp.route('/')
def index():
    db = get_db()
    books = db.execute('SELECT * FROM book').fetchall()
    return render_template('library/index.html', books=books)

@bp.route('/book/<int:id>')
def book_detail(id):
    db = get_db()
    book = db.execute('SELECT * FROM book WHERE id = ?', (id,)).fetchone()
    if book is None:
        abort(404, f"Book id {id} doesn't exist.")
    return render_template('library/book_detail.html', book=book)
