from flask import Blueprint, abort, jsonify, request
from accounts.app import api_info
from marshmallow_jsonschema import JSONSchema
from flask_jwt_extended import jwt_required, get_jwt_identity

from accounts.app.models import Bill, db
from accounts.app.schemas import BillSchema


bills = Blueprint('bills', __name__)

json_schema = JSONSchema()
bill_schema = BillSchema()


@api_info.resource('счет', '/bills/<id>', schema=json_schema.dump(bill_schema),
                   desc='Bill information')
@bills.route('/<int:id>')
def get_bill(id):
    bill = Bill.query.get(id)
    if not bill:
        abort(404)
    return jsonify(bill=bill_schema.dump(bill))


@api_info.action('открыть', '/bills', desc='Open bill')
@bills.route('', methods=['POST'])
@jwt_required
def create_bill():
    account_id = get_jwt_identity()
    bill = Bill(account_id=account_id)
    db.session.add(bill)
    db.session.commit()
    return jsonify({
        'message': 'succeed'
    }), 201
