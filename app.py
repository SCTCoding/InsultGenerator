#!/usr/bin/env python3

from flask import Flask, jsonify, request
import random

app = Flask(__name__)

# Text Source: https://www.scholastic.com/content/dam/teachers/articles/migrated-files-in-body/shakespeare_insult_kit.pdf

c1 = ["artless","bawdy","beslubbering","bootless","churlish","cockered","clouted","craven","currish","dankish","dissembling","droning","errant","fawning","fobbing","froward","frothy","gleeking","goatish","gorbellied","impertinent","infectious","jarring","loggerheaded","lumpish","mammering","mangled","mewling","paunchy","pribbling","puking","puny","qualling","rank","reeky","roguish","ruttish","saucy","spleeny","spongy","surly","tottering","unmuzzled","vain","venomed","villainous","warped","wayward","weedy","yeasty"]

c2 = ["base-court", "bat-fowling", "beef-witted", "beetle-headed", "boil-brained", "clapper-clawed", "clay-brained", "common-kissing", "crook-pated", "dismal-dreaming", "dizzy-eyed", "doghearted", "dread-bolted", "earth-vexing", "elf-skinned", "fat-kidneyed", "fen-sucked", "flap-mouthed", "fly-bitten", "folly-fallen", "fool-born", "full-gorged", "guts-griping", "half-faced", "hasty-witted", "hedge-born", "hell-hated", "idle-headed", "ill-breeding", "ill-nurtured", "knotty-pated", "milk-livered", "motley-minded", "onion-eyed", "plume-plucked", "pottle-deep", "pox-marked", "reeling-ripe", "rough-hewn", "rude-growing", "rump-fed", "shard-borne", "sheep-biting", "spur-galled", "swag-bellied", "tardy-gaited", "tickle-brained", "toad-spotted", "unchin-snouted", "weather-bitten"]

c3 = ["apple-john", "baggage", "barnacle", "bladder", "boar-pig", "bugbear", "bum-bailey", "canker-blossom", "clack-dish", "clotpole", "coxcomb", "codpiece", "death-token", "dewberry", "flap-dragon", "flax-wench", "flirt-gill", "foot-licker", "fustilarian", "giglet", "gudgeon", "haggard", "harpy", "hedge-pig", "horn-beast", "hugger-mugger", "joithead", "lewdster", "lout", "maggot-pie", "malt-worm", "mammet", "measle", "minnow", "miscreant", "moldwarp", "mumble-news", "nut-hook", "pigeon-egg", "pignut", "puttock", "pumpion", "ratsbane", "scut", "skainsmate", "strumpet", "varlot", "vassal", "whey-face", "wagtail"]

last_responses = []

def store_response(response):
    if len(last_responses) >= 10:
        last_responses.pop(0)
    last_responses.append(response)

@app.route('/', methods=['GET'])
def main():
	word1 = random.choice(c1)
	word2 = random.choice(c2)
	word3 = random.choice(c3)
	response = f'{word1} {word2} {word3}'

	store_response(response)
	
	return f'<h1>{word1} {word2} {word3}</h1>\n\n\n<h3>{last_responses}</h3>'

@app.route('/api', methods=['GET'])
def getInsult():
	word1 = random.choice(c1)
	word2 = random.choice(c2)
	word3 = random.choice(c3)
	data = [word1, word2, word3]

	store_response(' '.join(data))
		
	return jsonify(data)

@app.route('/last10', methods=['GET'])
def get_last_10_responses():
    return jsonify(last_responses)

@app.errorhandler(400)
def bad_request(error):
    response = jsonify({'error': 'Bad Request', 'message': str(error)})
    response.status_code = 400
    return response

if __name__ == '__main__':
	main()
