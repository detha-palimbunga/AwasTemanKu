
from flask import Flask, abort, send_from_directory

app = Flask(__name__)

@app.route("/")
def home():
    return send_from_directory(app.root_path, "index.html")

@app.route("/templates/<image_name>")
@app.route("/game-images/<image_name>")
def game_image(image_name):
    if image_name not in {"playergame.png", "ulanggame.png"}:
        abort(404)
    return send_from_directory(app.template_folder, image_name)

if __name__ == "__main__":
    app.run(debug=True)
