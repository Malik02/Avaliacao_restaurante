import pandas as pd
from flask import Flask, request, Response
import os

# Load data from CSV file

df = pd.read_csv('https://github.com/Malik02/Avaliacao_restaurante/blob/f56ed85110d75ec7cf589aed6a54063a6f56c1d6/Estabelecimento.csv')
dfava = pd.read_csv('https://github.com/Malik02/Avaliacao_restaurante/blob/f56ed85110d75ec7cf589aed6a54063a6f56c1d6/Avaliacoes.csv')
dfdias = pd.read_csv('https://github.com/Malik02/Avaliacao_restaurante/blob/f56ed85110d75ec7cf589aed6a54063a6f56c1d6/FuncionamentoDias.csv')
dfhorario = pd.read_csv('https://github.com/Malik02/Avaliacao_restaurante/blob/f56ed85110d75ec7cf589aed6a54063a6f56c1d6/FuncionamentoHorarios.csv')
dflocal = pd.read_csv('https://github.com/Malik02/Avaliacao_restaurante/blob/f56ed85110d75ec7cf589aed6a54063a6f56c1d6/Localizacao.csv')
dfpolmedia = pd.read_csv('https://github.com/Malik02/Avaliacao_restaurante/blob/f56ed85110d75ec7cf589aed6a54063a6f56c1d6/PolaridadeMedia.csv')
dfprincipais = pd.read_csv('https://github.com/Malik02/Avaliacao_restaurante/blob/f56ed85110d75ec7cf589aed6a54063a6f56c1d6/PrincipaisPalavras.csv')
dfserv = pd.read_csv('https://github.com/Malik02/Avaliacao_restaurante/blob/f56ed85110d75ec7cf589aed6a54063a6f56c1d6/Servico.csv')

# Remove the print statement
# print(df.to_json(orient="records"))

app = Flask(__name__)

# Add a route to return the entire df as JSON
@app.route("/", methods=['GET'])
def get_csv():
    return Response(df.to_json(orient="records"), mimetype='application/json')

# Fix the function name to match the endpoint URL
@app.route("/estabelecimento", methods=['GET'])
def get_estabelecimento():
    # Convert the input parameter to string and uppercase
    cod = str(request.args.get('cod')).upper()
    prod = df.loc[df['Nome'].str.upper() == cod]
    return Response(prod.to_json(orient="records"), mimetype='application/json')

# Fix the function name to match the endpoint URL
@app.route("/avaliacoes", methods=['GET'])
def get_avaliacoes():
    # Convert the input parameter to string and uppercase
    cod = str(request.args.get('cod')).upper()
    prod = dfava.loc[dfava['idEstabelecimento'].str.upper() == cod]
    return Response(prod.to_json(orient="records"), mimetype='application/json')

# Fix the function name to match the endpoint URL
@app.route("/diasfuncionamento", methods=['GET'])
def get_dasfuncionamento():
    # Convert the input parameter to string and uppercase
    cod = str(request.args.get('cod')).upper()
    prod = dfdias.loc[dfdias['Estabelecimento_ID'].str.upper() == cod]
    return Response(prod.to_json(orient="records"), mimetype='application/json')

# Fix the function name to match the endpoint URL
@app.route("/horarios", methods=['GET'])
def get_horarios():
    # Convert the input parameter to string and uppercase
    cod = str(request.args.get('cod')).upper()
    prod = dfhorario.loc[dfhorario['Estabelecimento_ID'].str.upper() == cod]
    return Response(prod.to_json(orient="records"), mimetype='application/json')

# Fix the function name to match the endpoint URL
@app.route("/localizacao", methods=['GET'])
def get_localizacao():
    # Convert the input parameter to string and uppercase
    cod = str(request.args.get('cod')).upper()
    prod = dflocal.loc[dflocal['Estabelecimento_ID'].str.upper() == cod]
    return Response(prod.to_json(orient="records"), mimetype='application/json')

# Fix the function name to match the endpoint URL
@app.route("/polaridade", methods=['GET'])
def get_polaridade():
    # Convert the input parameter to string and uppercase
    cod = str(request.args.get('cod')).upper()
    prod = dfpolmedia.loc[dfpolmedia['Estabelecimento_ID'].str.upper() == cod]
    return Response(prod.to_json(orient="records"), mimetype='application/json')

# Fix the function name to match the endpoint URL
@app.route("/principaispalavras", methods=['GET'])
def get_principaispalavras():
    # Convert the input parameter to string and uppercase
    cod = str(request.args.get('cod')).upper()
    prod = dfprincipais.loc[dfprincipais['Nome'].str.upper() == cod]
    return Response(prod.to_json(orient="records"), mimetype='application/json')

# Fix the function name to match the endpoint URL
@app.route("/servico", methods=['GET'])
def get_servico():
    # Convert the input parameter to string and uppercase
    cod = str(request.args.get('cod')).upper()
    prod = dfserv.loc[dfserv['Estabelecimento_ID'].str.upper() == cod]
    return Response(prod.to_json(orient="records"), mimetype='application/json')


if __name__ == "__main__":
    # Change the port number to avx oid conflicts
    app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 2100))