from flask import Flask, jsonify, request
# from pyngrok import ngrok

app = Flask(__name__)

# public_url = ngrok.connect(5000)
# print(public_url)

# Dados das carteiras de criptomoedas (exemplo)
carteiras = []

# Rota para criar uma nova carteira de criptomoedas
@app.route('/carteiras', methods=['POST'])
def criar_carteira():
    dados = request.get_json()
    nova_carteira = {
        'id': len(carteiras) + 1,
        'nome': dados['nome'],
        'saldo': 0.0,
        'criptomoedas': []
    }
    carteiras.append(nova_carteira)
    return jsonify(nova_carteira), 201

# Rota para consultar o saldo de uma carteira
@app.route('/carteiras/<int:carteira_id>/saldo', methods=['GET'])
def consultar_saldo(carteira_id):
    for carteira in carteiras:
        if carteira['id'] == carteira_id:
            return jsonify({'saldo': carteira['saldo']})
    return jsonify({'mensagem': 'Carteira não encontrada'}), 404

# Rota para adicionar criptomoedas a uma carteira
@app.route('/carteiras/<int:carteira_id>/adicionar', methods=['PUT'])
def adicionar_criptomoedas(carteira_id):
    dados = request.get_json()
    quantidade = dados['quantidade']
    criptomoeda = dados['criptomoeda']

    for carteira in carteiras:
        if carteira['id'] == carteira_id:
            carteira['saldo'] += quantidade
            carteira['criptomoedas'].append(criptomoeda)
            return jsonify({'mensagem': 'Criptomoedas adicionadas com sucesso!'})
    return jsonify({'mensagem': 'Carteira não encontrada'}), 404

# Rota para remover criptomoedas de uma carteira
@app.route('/carteiras/<int:carteira_id>/remover', methods=['PUT'])
def remover_criptomoedas(carteira_id):
    dados = request.get_json()
    quantidade = dados['quantidade']
    criptomoeda = dados['criptomoeda']

    for carteira in carteiras:
        if carteira['id'] == carteira_id:
            if criptomoeda in carteira['criptomoedas']:
                if carteira['saldo'] >= quantidade:
                    carteira['saldo'] -= quantidade
                    carteira['criptomoedas'].remove(criptomoeda)
                    return jsonify({'mensagem': 'Criptomoedas removidas com sucesso!'})
                else:
                    return jsonify({'mensagem': 'Saldo insuficiente na carteira'}), 400
            else:
                return jsonify({'mensagem': 'Criptomoeda não encontrada na carteira'}), 404
    return jsonify({'mensagem': 'Carteira não encontrada'}), 404

# Rota para transferir criptomoedas entre carteiras
@app.route('/carteiras/<int:carteira_origem_id>/transferir', methods=['PUT'])
def transferir_criptomoedas(carteira_origem_id):
    dados = request.get_json()
    carteira_destino_id = dados['carteira_destino']
    quantidade = dados['quantidade']
    criptomoeda = dados['criptomoeda']

    for carteira_origem in carteiras:
        if carteira_origem['id'] == carteira_origem_id:
            if criptomoeda in carteira_origem['criptomoedas']:
                if carteira_origem['saldo'] >= quantidade:
                    for carteira_destino in carteiras:
                        if carteira_destino['id'] == carteira_destino_id:
                            carteira_origem['saldo'] -= quantidade
                            carteira_destino['saldo'] += quantidade
                            carteira_origem['criptomoedas'].remove(criptomoeda)
                            carteira_destino['criptomoedas'].append(criptomoeda)
                            return jsonify({'mensagem': 'Transferência realizada com sucesso!'})
                    return jsonify({'mensagem': 'Carteira destino não encontrada'}), 404
                else:
                    return jsonify({'mensagem': 'Saldo insuficiente na carteira de origem'}), 400
            else:
                return jsonify({'mensagem': 'Criptomoeda não encontrada na carteira de origem'}), 404
    return jsonify({'mensagem': 'Carteira de origem não encontrada'}), 404

# Rota para excluir uma carteira
@app.route('/carteiras/<int:carteira_id>', methods=['DELETE'])
def excluir_carteira(carteira_id):
    for carteira in carteiras:
        if carteira['id'] == carteira_id:
            carteiras.remove(carteira)
            return jsonify({'mensagem': 'Carteira excluída com sucesso!'})
    return jsonify({'mensagem': 'Carteira não encontrada'}), 404

# Rota para consultar o histórico de transações de uma carteira
@app.route('/carteiras/<int:carteira_id>/historico', methods=['GET'])
def consultar_historico(carteira_id):
    for carteira in carteiras:
        if carteira['id'] == carteira_id:
            return jsonify({'historico': carteira['historico']})
    return jsonify({'mensagem': 'Carteira não encontrada'}), 404

# Rota para comprar criptomoedas através de uma corretora (simulação)
@app.route('/carteiras/<int:carteira_id>/comprar', methods=['POST'])
def comprar_criptomoedas(carteira_id):
    dados = request.get_json()
    corretora = dados['corretora']
    quantidade = dados['quantidade']
    criptomoeda = dados['criptomoeda']

    # Lógica para compra de criptomoedas através da corretora (simulada)

    for carteira in carteiras:
        if carteira['id'] == carteira_id:
            carteira['saldo'] += quantidade
            carteira['criptomoedas'].append(criptomoeda)
            return jsonify({'mensagem': 'Compra realizada com sucesso!'})
    return jsonify({'mensagem': 'Carteira não encontrada'}), 404

# Rota para vender criptomoedas através de uma corretora (simulação)
@app.route('/carteiras/<int:carteira_id>/vender', methods=['POST'])
def vender_criptomoedas(carteira_id):
    dados = request.get_json()
    corretora = dados['corretora']
    quantidade = dados['quantidade']
    criptomoeda = dados['criptomoeda']

    # Lógica para venda de criptomoedas através da corretora (simulada)

    for carteira in carteiras:
        if carteira['id'] == carteira_id:
            if criptomoeda in carteira['criptomoedas']:
                if carteira['saldo'] >= quantidade:
                    carteira['saldo'] -= quantidade
                    carteira['criptomoedas'].remove(criptomoeda)
                    return jsonify({'mensagem': 'Venda realizada com sucesso!'})
                else:
                    return jsonify({'mensagem': 'Saldo insuficiente na carteira'}), 400
            else:
                return jsonify({'mensagem': 'Criptomoeda não encontrada na carteira'}), 404
    return jsonify({'mensagem': 'Carteira não encontrada'}), 404

if __name__ == '__main__':
    app.run(debug=True)
