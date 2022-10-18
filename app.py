from flask import Flask, render_template

app = Flask(__name__)

exhibits = [
    {
        "id": 1,
        "name": "Television History"
    },
    {
        "id": 2,
        "name": "Car History"
    }
]

items = [
    {
        "id": 1,
        "name":  "Flinstones",
        "exhibit_id": 1,
        "image_url": "https://m.media-amazon.com/images/M/MV5BZmYxZjE2MDYtYTQ2OC00NmUwLTkzNDEtNjFkZmEyM2E5ODBmXkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_.jpg"
    },
    {
        "id": 2,
        "name":  "Jetsons",
        "exhibit_id": 1,
        "image_url": "https://m.media-amazon.com/images/M/MV5BYmIwY2I1ZGEtYzI3Mi00OTYwLWJkZjktNDQxMDlhMzM3MmU2XkEyXkFqcGdeQXVyNjc0MzMzNjA@._V1_.jpg"
    },
    {
        "id": 3,
        "name":  "Scooby-Doo",
        "exhibit_id": 1,
        "image_url": "https://media-cldnry.s-nbcnews.com/image/upload/rockcms/2021-06/210615-scooby-doo-al-1315-25fdf5.jpg"
    }
]



@app.route("/")
def root():
    return "<h1>Root</h1>"

@app.route("/exhibits/<id>")
def exhibit_index(id):

    exhibit = filter(lambda x: x.id == int(id), exhibits)

    items_list = list(filter(lambda x: x.get('exhibit_id') == int(id), items))

    print(items_list)

    return render_template('exhibit.html', items=items_list)
