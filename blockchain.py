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
                 } # a block is implemented by a dictionary
        self.chain.append(block)
        return block

    def get_previous_block(self):
        #give the last block of the chain
        return self.chain[-1]

    def proof_of_work(self, previous_proof):
        #take only the previous proof and the new_proof
        #can traverse from 0 as well
        new_proof = 1
        #once find the proof will cmake true check_proof
        check_proof = False
        while check_proof is False:
            # need to be non symmetrical, or two proofs would be equal;
            # could be more complex(in real world this is changed to hash the data field of the block object)
            # encode to be readable by sha-256 and convert the result to hex number
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()

            # check if first four character are 0s(target value); hash_operation is string
            if hash_operation[0:4] == '0000':
                check_proof = True
            else:
                new_proof += 1

        #find the new_proof(the Nounce val)
        return new_proof

    def proof_of_work_take_entire_expected_block(self, expected_block):
        new_proof = 1
        check_proof = False
        while check_proof is False:
            expected_output = hash(expected_block)
            # random target '0000'
            if expected_output[:4] == '0000':
                check_proof = True
            else:
                new_proof += 1
        return new_proof


    def hash(self, block):
        # hash a block: generate the current hash code for the entire block: the finger print
        # use json library to make the block a string
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()


    def is_chain_valid(self, chain):
        # iterate the whole chain to check if this chain is valid
        previous_block = chain[0]
        block_index = 1
        while block_index < len(chain):
            curr_block = chain[block_index]
            #check if the previous_hash key of the current block equals to the previous block hash
            if curr_block['previous_hash'] != self.hash(previous_block):
                return False
            # check if the current proof of work reaches the target
            previous_proof = previous_block['proof']
            curr_proof = curr_block['proof']
            hash_operation = hashlib.sha256(str(curr_proof ** 2 - previous_proof ** 2).encode()).hexdigest()
            if hash_operation[:4] != '0000':
                return False

            previous_block = curr_block
            block_index += 1

        return True



#part 2 - Mining our Blockchain