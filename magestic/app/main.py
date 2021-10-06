from flask import Flask, render_template, redirect, url_for, session, request
from urllib.parse import urlparse
import shlex
import subprocess
import os


app = Flask(__name__)

# GLOBAL
# ======================
CURL_CMD = "curl -sS {}"
FLAG = os.environ.get("FLAG") or "DUMMY{THIS_IS_DUMMY}"
# ======================


def sanitize(fqdn: str) -> str:
    requires = ["http"]
    restricts = ["127", "192", "172", "10", "0"]

    sanitized_fqdn = shlex.quote(fqdn)

    scheme = urlparse(sanitized_fqdn).scheme
    # str: "https://foo.bar:443/hoge/fuga" -> list: ["foo", "bar"]
    netloc = urlparse(sanitized_fqdn).netloc.split(":")[0].split(".")
    port   = urlparse(sanitized_fqdn).netloc.split(":")[1]
    path   = urlparse(sanitized_fqdn).path

    # check netloc[0] can be int
    try:
        if len(netloc) != 4: raise
        for octet in netloc:
            int(octet)
            if len(octet) > 4: raise
    except:
        raise ValueError("ERR: Require IP Address")

    # check require parameter
    for require in requires:
        if not require == scheme:
            raise ValueError("ERR: Does not contain require words!")

    # check restrict parameter
    for restrict in restricts:
        if restrict == netloc[0]:
            raise ValueError("ERR: Do not contain prohibited words!")


    
    conn_addr = f"{scheme}://{int(netloc[0])}.{int(netloc[1])}.{int(netloc[2])}.{int(netloc[3])}:{port}{path}"
    print(conn_addr)
    query = CURL_CMD.format(conn_addr)
    curl_proc = subprocess.run(query, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if curl_proc.stderr == b"":
        return curl_proc.stdout
    else:
        return curl_proc.stderr


@app.route("/")
def page_main():
    return render_template("index.html")

@app.route("/ezpz")
def page_ezpz():
    if request.remote_addr == "127.0.0.1":
        return FLAG
    else:
        return "Your IP is {}".format(request.remote_addr)


@app.route("/api/request", methods=["POST"])
def page_api():
    fqdn = request.form["fqdn"]
    try:
        harmless_fqdn = sanitize(fqdn)
    except Exception as e:
        return str(e)
    else:
        return harmless_fqdn


if __name__ == "__main__":
    #app.run(debug=True, host="0.0.0.0", port=5000)
    app.run(host="127.0.0.1", port=30501)

