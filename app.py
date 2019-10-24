from flask import Flask
import add_text

app = Flask(__name__, static_url_path="/static/")

@app.route("/")
def main_page():
    add_text.add_bottom_text()
    return """
    <! DOCTYPE>
    <html>
        <head>
            <title>BOTTOM TEXT</title>
        </head>
        <body>
            <img src="static/btm-txt.jpg" alt="test"></img>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run()
