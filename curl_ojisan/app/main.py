from flask import Flask, render_template, redirect, url_for, session, request
import shlex
import subprocess


app = Flask(__name__)

# GLOBAL
# ======================
CURL_CMD = "curl -sS {}"
FLAG = "yuruhack{THIS_IS_NOT_FLAG}"
# ======================


def sanitize(fqdn: str) -> str:
    requires = ["http://"]
    restricts = ["127.","192.168.","172.","10.","::1", "localhost", "[", "]", "file"]
    sani_fqdn = shlex.quote(fqdn)
    query = CURL_CMD.format(sani_fqdn)

    for require in requires:
        if not require in sani_fqdn:
            raise ValueError("Does not contain require words!")
    for restrict in restricts:
        if restrict in sani_fqdn:
            raise ValueError("Do not contain prohibited words!")
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
    app.run(host="0.0.0.0", port=80)

