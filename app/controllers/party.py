from flask import request, jsonify
from app import application as app
from app.models.party import *
from app.const import *
from app.controllers.url import *
from app import isOnDev

@app.route('/party', methods=['GET', 'POST'])
def party():

    construct = {
        'success': False,
        'message': 'Method not allowed :)'
    }
    response = jsonify(construct)
    response.status_code = HttpStatus.NOT_ALLOWED

    #   Get all from table party
    if request.method == 'GET':
        construct = {
            'success': True,
            'parties': Party.getAll()
        }
        response = jsonify(construct)
        response.status_code = HttpStatus.OK

    #   Trying to insert into the table
    elif request.method == 'POST' and isOnDev:

        #   Trying to get parameters from the POST method
        try:
            name = EmptyValues.EMPTY_STRING if request.json['name'] == EmptyValues.EMPTY_STRING else request.json['name']
            abbreviation = EmptyValues.EMPTY_STRING if request.json['abbreviation'] == EmptyValues.EMPTY_STRING else request.json['abbreviation']
            colors = EmptyValues.EMPTY_STRING if request.json['colors'] == EmptyValues.EMPTY_STRING else request.json['colors']
            area_id = EmptyValues.EMPTY_INT if request.json['area_id'] == EmptyValues.EMPTY_STRING else request.json['area_id']
            coalition_id = EmptyValues.EMPTY_INT if request.json['coalition_id'] == EmptyValues.EMPTY_STRING else request.json['coalition_id']

            #   Verifying REQUIRED values
            if name == EmptyValues.EMPTY_STRING:
                construct['success'] = False
                construct['error'] = 'Missing data. Required values for name.'
                response = jsonify(construct)
                response.status_code = HttpStatus.BAD_REQUEST
                return response

            #   Trying to INSERT into the DB
            try:
                party = Party(
                    name=name, abbreviation=abbreviation, colors=colors,
                    area_id=area_id, coalition_id=coalition_id
                )
                party.save()
                construct['success'] = True
                construct['message'] = 'Data saved'
                response = jsonify(construct)
                response.status_code = HttpStatus.CREATED

            #   Falling while INSERTING into the DB
            except Exception as e:
                construct['success'] = False
                construct['error'] = str(e)
                response = jsonify(construct)
                response.status_code = HttpStatus.BAD_REQUEST

        #   Missing parameters from the POST method
        except Exception as e:
            construct['success'] = False
            construct['error'] = 'Missing data. Missing value ' + str(e)
            response = jsonify(construct)
            response.status_code = HttpStatus.BAD_REQUEST

    return response

@app.route('/party/<int:party_id>', methods=['GET', 'PUT', 'DELETE'])
def partyId(party_id):

    construct = {
        'success': False,
        'message': 'Method not allowed :)'
    }
    response = jsonify(construct)
    response.status_code = HttpStatus.NOT_ALLOWED

    #   Trying to get the area with area_id
    party = Party.query.filter_by(party_id=party_id).first()

    #   If theres no result from the above query
    if not party:
        construct = {
            'success': False,
            'message': 'Theres no data for that party_id'
        }
        response = jsonify(construct)
        response.status_code = HttpStatus.OK
        return response

    #   If theres a result, then ...
    #   Get their data
    if request.method == 'GET':
        construct = {
            'success': True,
            'party': {
                'id': party.party_id,
                'name': {
                    'en_US': party.name,
                    'es_MX': party.name
                },
                'abbreviation': {
                    'en_US': party.abbreviation,
                    'es_MX': party.abbreviation
                },
                'colors': party.colors,
                'area_id': "" if party.area_id == EmptyValues.EMPTY_INT else party.area_id,
                'coalition_id': "" if party.coalition_id == EmptyValues.EMPTY_INT else party.coalition_id,
                'fb_urls': Url.get_party_or_coalition_fb_urls(party.party_id, URL_OWNER_TYPE.PARTY),
                'ig_urls': Url.get_party_or_coalition_ig_urls(party.party_id, URL_OWNER_TYPE.PARTY),
                'logo_urls': Url.get_party_or_coalition_logo_urls(party.party_id, URL_OWNER_TYPE.PARTY),
                'websites': Url.get_party_or_coalition_or_person_websites_urls(party.party_id, URL_OWNER_TYPE.PARTY)
            }
        }
        response = jsonify(construct)
        response.status_code = HttpStatus.OK

    #   Update their data
    elif request.method == 'PUT' and isOnDev:

        #   Trying to get parameters from the PUT method
        try:
            name = EmptyValues.EMPTY_STRING if request.json['name'] == EmptyValues.EMPTY_STRING else request.json['name']
            abbreviation = EmptyValues.EMPTY_STRING if request.json['abbreviation'] == EmptyValues.EMPTY_STRING else request.json['abbreviation']
            colors = EmptyValues.EMPTY_STRING if request.json['colors'] == EmptyValues.EMPTY_STRING else request.json['colors']
            area_id = EmptyValues.EMPTY_INT if request.json['area_id'] == EmptyValues.EMPTY_STRING else request.json['area_id']
            coalition_id = EmptyValues.EMPTY_INT if request.json['coalition_id'] == EmptyValues.EMPTY_STRING else request.json['coalition_id']

            #   Verifying REQUIRED values
            if name == EmptyValues.EMPTY_STRING:
                construct['success'] = False
                construct['error'] = 'Missing data. Required values for name.'
                response = jsonify(construct)
                response.status_code = HttpStatus.BAD_REQUEST
                return response

            #   Trying to UPDATE into the DB
            try:
                party.name = name
                party.abbreviation = abbreviation
                party.colors = colors
                party.area_id = area_id
                party.coalition_id = coalition_id
                db.session.commit()
                construct['success'] = True
                construct['message'] = 'Data saved'
                response = jsonify(construct)
                response.status_code = HttpStatus.CREATED

            #   Falling while UPDATING into the DB
            except Exception as e:
                construct['success'] = False
                construct['error'] = str(e)
                response = jsonify(construct)
                response.status_code = HttpStatus.BAD_REQUEST

        #   Missing parameters from the PUT method
        except Exception as e:
            construct['success'] = False
            construct['error'] = 'Missing data. Missing value ' + str(e)
            response = jsonify(construct)
            response.status_code = HttpStatus.BAD_REQUEST

    #   Delete it from the database
    elif request.method == 'DELETE' and isOnDev:

        try:
            party.delete()
            construct['success'] = True
            construct['message'] = 'Data has been delete.'
            response = jsonify(construct)
            response.status_code = HttpStatus.OK
        except Exception as e:
            construct['success'] = False
            construct['error'] = str(e)
            response = jsonify(construct)
            response.status_code = HttpStatus.BAD_REQUEST
            
    return response
