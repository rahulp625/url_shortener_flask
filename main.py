# main.py 

from flask import Flask, json, request, redirect, jsonify
from math import floor
import sqlite3
from urllib.parse import urlparse

host = 'http://127.0.0.1:5001/'


# Base62 Encoder and Decoder
def toBase62(num):
    b = 62
    base = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    r = num % b
    res = base[r];
    q = floor(num / b)
    while q:
        r = q % b
        q = floor(q / b)
        res = base[int(r)] + res
    return res

def toBase10(num):
    # base = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    limit = len(num)
    res = 0
    for i in range(limit):
        # res = b * res + base.find(num[i])
        val_i = ord(num[i])
        if(val_i >= ord('a') and val_i <= ord('z')):
            res = res*62 + val_i - ord('a')
        elif(val_i >= ord('A') and val_i <= ord('Z')):
            res = res*62 + val_i - ord('Z') + 26
        else:
            res = res*62 + val_i - ord('0') + 52        
    return res


app = Flask(__name__)

# Home page where user should enter 
@app.route('/post_url', methods=['POST'])
def home():
    if request.method == 'POST':
        original_url = request.json.get('url')
        if urlparse(original_url).scheme == '':
            original_url = 'http://' + original_url
        with sqlite3.connect('urls.db') as conn:
            cursor = conn.cursor()
            insert_row = """
                INSERT INTO WEB_URL (original_url)
                    VALUES ('%s')
                """%(original_url)
            result_cursor = cursor.execute(insert_row)
            encoded_string = toBase62(result_cursor.lastrowid)

        return jsonify(
            short_url= host + encoded_string
        )


@app.route('/<short_url>')
def redirect_short_url(short_url):
    decoded_string = toBase10(short_url)
    redirect_url = 'http://localhost:5001'
    with sqlite3.connect('urls.db') as conn:
        cursor = conn.cursor()
        select_row = """
                SELECT original_url FROM WEB_URL
                    WHERE ID=%s
                """%(decoded_string)
        result_cursor = cursor.execute(select_row)
        try:
            redirect_url = result_cursor.fetchone()[0]
        except Exception as e:
            print(e)
    return redirect(redirect_url)


if __name__ == '__main__':
    # This code checks whether database table is created or not
    app.run(host="0.0.0.0", port="5001", debug=True)
