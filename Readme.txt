Steps-

1) Run pip install -r requirements.txt
2) Run python init_db.py
3) Run python main.py

For running dockerized version-

1) Run docker pull rahulp4112/url-shortener-flask
2) Run docker run --name url_shortener_flask_running -p 5001:5001 rahulp4112/url-shortener-flask



APIs- 
1) POST - http://localhost:5001/post_url

Data format-

{
    "url": "https://hub.docker.com/"
}

Output format -

{
    "short_url": "http://127.0.0.1:5001/b"
}


Open browser and type - http://127.0.0.1:5001/b. You should be redirected to https://hub.docker.com/.
