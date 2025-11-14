from flask import render_template, url_for, redirect, request, flash
from flask_login import login_required
from extensions import db
from models import Inventory
from . import store_bp
import pandas as pd

# @store_bp.route('/')
# @login_required
# def index():
#     records = Inventory.query.all()
#     return render_template('store/index.html', title='Magazyn', records=records)

@store_bp.route('/', methods=['GET', 'POST'])
@login_required
def index():
    page = request.args.get('page', 1, type=int)
    per_page = 20
    search = request.args.get('search', '').strip()
    query = Inventory.query
    if search:
        query = query.filter(
            Inventory.name.ilike(f'%{search}%') |
            Inventory.symbol.ilike(f'%{search}%') |
            Inventory.category.ilike(f'%{search}%') |
            Inventory.brand.ilike(f'%{search}%') |
            Inventory.model.ilike(f'%{search}%')
        )
    pagination = query.order_by(Inventory.id).paginate(page=page, per_page=per_page)
    records = pagination.items
    return render_template('store/index.html', title='Magazyn', records=records, pagination=pagination, search=search)

@store_bp.route('/import', methods=['POST'])
@login_required
def import_data():
    # pobranie pliku z formularza
    file = request.files.get('file')
    if not file:
        flash('Nie wybrano pliku!', 'danger')
        return redirect(url_for('store.index'))

    # wczytywanie zawartości csv do data frame za pomocą pandas
    try:
        df = pd.read_csv(file)
    except Exception as e:
        flash(f'Błąd wczytywania pliku: {e}', 'danger')
        return redirect(url_for('store.index'))

    # usuń istniejące rekordy
    db.session.query(Inventory).delete()

    # dodanie rekordów do bazy
    for _, row in df.iterrows():
        item = Inventory(
            id=int(row['id']),
            symbol=row['symbol'],
            name=row['name'],
            category=row['category'],
            brand=row['brand'],
            model=row['model'],
            quantity=int(row['quantity']),
            weight_kg=float(row['weight_kg']),
            price_pln=float(row['price_pln']),
            inventory_value_pln=float(row['inventory_value_pln'])
        )
        db.session.add(item)

    db.session.commit()
    flash('Dane zostały zaimportowane pomyślnie!', 'success')
    return redirect(url_for('store.index'))