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
        # use this after a block is mined: use this after finding the proof using 'proof of work': define the problem
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

    def proof_of_work(self, previous_proof):
        #increment new_proof in while loop
        #can traverse from 0 as well
        new_proof = 1
        #once find the proof will cmake true check_proof
        check_proof = False
        while check_proof is False:
            # need to be non symmetrical, or two proofs would be equal; could be more complex(actually can change it to hash the whole content of block)
            # encode to be readable by sha-256 and convert the result to hex number
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()

            # check if first four character are 0s(target value); hash_operation is string
            if hash_operation[0:4] == '0000':
                check_proof = True
            else:
                new_proof += 1

            #find the new_proof(the Nounce val)
            return new_proof



#part 2 - Mining our Blockchain