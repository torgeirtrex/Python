# main.py
from sqlalchemy.dialects import mysql

from app import app
from db_setup import init_db, db_session
from forms import MusicSearchForm, AlbumForm
from flask import flash, render_template, request, redirect, send_file, Flask, make_response, Response
from models import Album, Artist
from tables import Results
from io import BytesIO
from flask_sqlalchemy import SQLAlchemy
import sqlite3
from sqlite3 import Error
import os
import csv
import pandas as pd
import io
import pymysql
import MySQLdb




'''from mysql import mysql.connector'''

init_db()

'''
Features added
22.10. Added validation to new album form
23.10 Wikipedia search from index with javascript: https://www.youtube.com/watch?v=Um8ZfL3Qfvw
09.11 Added flash message when creating new entries that names the latest added album 

Idea 1: Create machine learning model with HTML interface and return results
Idea 2: Create button to export database to CSV
https://stackoverflow.com/questions/33766499/flask-button-to-save-table-from-query-as-csv
https://www.youtube.com/watch?v=QPI3rzZow6k
https://gist.github.com/madan712/f27ac3b703a541abbcd63871a4a56636
https://stackoverflow.com/questions/54229962/how-to-programmatically-convert-multiple-db-files-to-csv-in-python-or-r
https://roytuts.com/generate-csv-report-from-mysql-database-using-python-flask/
'''


@app.route('/', methods=['GET', 'POST'])
def index():
    search = MusicSearchForm(request.form)
    if request.method == 'POST':
        return search_results(search)

    return render_template('index.html', form=search)


@app.route('/results')
def search_results(search):
    results = []
    search_string = search.data['search']
    if search_string:
        if search.data['select'] == 'Artist':
            qry = db_session.query(Album, Artist).filter(
                Artist.id==Album.artist_id).filter(
                    Artist.name.contains(search_string))
            results = [item[0] for item in qry.all()]
        elif search.data['select'] == 'Album':
            qry = db_session.query(Album).filter(
                Album.title.contains(search_string))
            results = qry.all()
        elif search.data['select'] == 'Publisher':
            qry = db_session.query(Album).filter(
                Album.publisher.contains(search_string))
            results = qry.all()
        else:
            qry = db_session.query(Album)
            results = qry.all()
    else:
        qry = db_session.query(Album)
        results = qry.all()
    if not results:
        flash('No results found!')
        return redirect('/')
    else:
        # display results
        table = Results(results)
        table.border = True
        return render_template('results.html', table=table)

@app.route('/new_album', methods=['GET', 'POST'])
def new_album():
    """
    Add a new album
    """
    form = AlbumForm(request.form)

    if request.method == 'POST' and form.validate():
        # save the album
        album = Album()
        save_changes(album, form, new=True)
        flash(f'You have successfully created the album {album.title} by {album.artist}!')
        return redirect('/')

    return render_template('new_album.html', form=form)

def save_changes(album, form, new=False):
    """
    Save the changes to the database
    """
    # Get data from form and assign it to the correct attributes
    # of the SQLAlchemy table object
    artist = Artist()
    artist.name = form.artist.data

    album.artist = artist
    album.title = form.title.data
    album.release_date = form.release_date.data
    album.publisher = form.publisher.data
    album.media_type = form.media_type.data

    if new:
        # Add the new album to the database
        db_session.add(album)

    # commit the data to the database
    db_session.commit()

@app.route('/item/<int:id>', methods=['GET', 'POST'])
def edit(id):
    qry = db_session.query(Album).filter(
                Album.id==id)
    album = qry.first()

    if album:
        form = AlbumForm(formdata=request.form, obj=album)
        if request.method == 'POST' and form.validate():
            # save edits
            save_changes(album, form)
            flash('Album updated successfully!')
            return redirect('/')
        return render_template('edit_album.html', form=form)
    else:
        return 'Error loading #{id}'.format(id=id)

@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    """
    Delete the item in the database that matches the specified
    id in the URL
    """
    qry = db_session.query(Album).filter(
        Album.id==id)
    album = qry.first()
    if album:
        form = AlbumForm(formdata=request.form, obj=album)
        if request.method == 'POST' and form.validate():
            # delete the item from the database
            db_session.delete(album)
            db_session.commit()
            flash('Album deleted successfully!')
            return redirect('/')
        return render_template('delete_album.html', form=form)
    else:
        return 'Error deleting #{id}'.format(id=id)

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['inputFile']
    return file.filename

@app.route('/')
def download():
	return render_template('download.html')

@app.route('/download/report/csv')
def download_report():
    '''
    C:/Users/torge/PycharmProjects/flask101/mymusic.db
    '''
    conn = sqlite3.connect("C:/Users/torge/PycharmProjects/flask101/mymusic.db", isolation_level=None,
                           detect_types=sqlite3.PARSE_COLNAMES)
    db_df = pd.read_sql_query("SELECT * FROM albums", conn)
    db_df.to_csv('database.csv', index=False)



if __name__ == '__main__':
    import os
    if 'WINGDB_ACTIVE' in os.environ:
        app.debug = False
    app.run(port=5001)