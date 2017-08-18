import os
from flask import Flask, render_template
import random
import sheltered as sheltered

#initialization
app = Flask(__name__)
app.config.update(
        DEBUG = True,
        )

@app.route('/')
def get_picture():
    picture_list = sheltered.find_picture()
    return render_template('show_entries.html',picture_list=picture_list)


# launch
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
