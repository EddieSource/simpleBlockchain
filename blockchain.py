# create a simple block chain

import datetime
import hashlib
import json
from flask import Flask, jsonify

#part 1 - build a blockchain
class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_block(proof=1, previous_hash='0')

    def create_block(self, proof, previous_hash):
        # create a block using a dictionary of generally 4 central keys
        # use this after a block is mined: need the proof based on 'proof of work': define the problem
        # can create more by adding the 'data' key (will use this in next module)
        block = {'index': len(self.chain) + 1,
                 'timestamp': datetime.datetime.now(), # return year,month,day,hour,min,sec
                 'proof': proof,
                 'previous_hash': previous_hash
                 }
        self.chain.append(block)
        return block

    def get_previous_block(self):
        #give the last block of the chain
        return self.chain[-1]

#part 2 - Mining our Blockchain