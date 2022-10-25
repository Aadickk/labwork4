import flask
from flask import Flask, request
import web3
import requests
import psycopg2
connect = psycopg2.connect(dbname='Hello', user='postgres',
                          password = 'postgres', host = 'localhost')
cursor = connect.cursor()
app = flask.Flask(__name__)
@app.route('/')
def index():
    return flask.render_template('index.html')
@app.route("/", methods=["GET", "POST"])
def index():
    token = database.nft
    address = request.form.get("password")
    if request.method == "POST":
        if database.get(address) != "":
            token = Connector.getTokenByDatabase(address)
        else:
            token = Connector.getTokenByRequest("mainnet", address)

    return render_template("index.html",
        mint=str(token.mint),
        stan=str(token.standard),
        name=str(token.name),
        symbol=str(token.symbol),
        metadataUrl=str(token.metaplex_metadataUrl),
        update=str(token.metaplex_updateAuthority),
        sellerFeeBasisPoint=str(token.metaplex_sellerFeeBasisPoints),
        primarySale=str(token.metaplex_primarySaleHappened),
        isMuta=str(token.metaplex_isMutable),
        master=str(token.metaplex_masterEdition),
        owners_address=str(token.metaplex_owners_address),
        owners_verified=str(token.metaplex_owners_verified),
        owners_share=str(token.metaplex_owners_share))
if __name__ == '__main__':
    app.debug=True
    app.run()


