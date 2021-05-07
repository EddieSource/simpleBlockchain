from blockchain import *
from flask import Flask, jsonify

#part 2 - Mining our Blockchain

# Creating a Web App based on Flask
app = Flask(__name__)
# app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

blockchain = Blockchain()


# CRUD get method
@app.route('/mine_block', methods=["GET"])
# mining a new block
def mine_block():
    prev_block = blockchain.get_previous_block()
    prev_proof = prev_block['proof']

    #main mining work: find the expected_proof
    curr_proof = blockchain.proof_of_work(prev_proof)

    #create and add the correctly mined block to our chain
    prev_hash = blockchain.hash(prev_block)
    curr_block = blockchain.create_block(curr_proof, prev_hash)
    # return a json object
    response = {'message': 'Congratulations, you just mined a block!',
                'index': curr_block['index'],
                'timestamp': curr_block['timestamp'],
                'proof': curr_block['proof'],
                'prev_hash': curr_block['previous_hash']}
    return jsonify(response), 200 # demo on postman:200 means everything is ok


# getting the full Blockchain
@app.route('/get_chain', methods=["GET"])
def get_chain():
    response = {'chain': blockchain.chain,
                'length': len(blockchain.chain)}
    return jsonify(response), 200


@app.route('/is_valid', methods=["GET"])
def is_valid():
    is_valid = blockchain.is_chain_valid(blockchain.chain)
    if is_valid:
        response = {'message': 'All good. The Blockchain is valid.'}
    else:
        response = {'message': 'Problem occurs. Blockchain is NOT valid'}

    return jsonify(response), 200


if __name__ == '__main__':
    # Running the app on http://127.0.0.1:5000/
    # use postman to test
    app.run(host='0.0.0.0', port=5000)