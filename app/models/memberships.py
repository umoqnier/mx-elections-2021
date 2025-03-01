from app import db
from app.const import Catalogues, EmptyValues
from datetime import date
from app.controllers.url import *

class Membership(db.Model):
    __tablename__ = 'membership'
    __table_args__ = {'sqlite_autoincrement': True}

    membership_id = db.Column(db.Integer, unique=True, primary_key=True, nullable=False, autoincrement=True)
    person_id = db.Column(db.Integer, db.ForeignKey('person.person_id'), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('role.role_id'), nullable=False)
    party_id = db.Column(db.Integer, db.ForeignKey('party.party_id'), nullable=False)
    #coalition_id = db.Column(db.Integer, db.ForeignKey('coalition.coalition_id'), nullable=True)
    coalition_id = db.Column(db.Integer, nullable=True)
    #contest_id = db.Column(db.Integer, db.ForeignKey('contest.contest_id'), nullable=True)
    contest_id = db.Column(db.Integer, nullable=True)
    goes_for_coalition = db.Column(db.Boolean, nullable=False)
    membership_type = db.Column(db.Integer, nullable=False)
    goes_for_reelection = db.Column(db.Boolean, nullable=False)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    is_substitute = db.Column(db.Boolean, nullable=False)
    #parent_membership_id = db.Column(db.Integer, db.ForeignKey('membership.membership_id'), nullable=True)
    parent_membership_id = db.Column(db.Integer, nullable=True)
    changed_from_substitute = db.Column(db.Boolean)
    date_changed_from_substitute = db.Column(db.Date)


    def __init__(
            self, person_id, role_id, party_id, coalition_id, contest_id, goes_for_coalition,
            membership_type, goes_for_reelection, start_date, end_date, is_substitute,
            parent_membership_id, changed_from_substitute, date_changed_from_substitute
        ):
        self.person_id = person_id
        self.role_id = role_id
        self.party_id = party_id
        self.coalition_id = coalition_id
        self.contest_id = contest_id
        self.goes_for_coalition = goes_for_coalition
        self.membership_type = membership_type
        self.goes_for_reelection = goes_for_reelection
        self.start_date = start_date
        self.end_date = end_date
        self.is_substitute = is_substitute
        self.parent_membership_id = parent_membership_id
        self.changed_from_substitute = changed_from_substitute
        self.date_changed_from_substitute = date_changed_from_substitute

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def getAll():
        memberships = Membership.query.all()
        result = []
        for membership in memberships:
            obj = {
                'id': membership.membership_id,
                'person_id': membership.person_id,
                'role_id': membership.role_id,
                'party_ids': [membership.party_id],
                'coalition_id': "" if membership.coalition_id == EmptyValues.EMPTY_INT else membership.coalition_id,
                'contest_id': "" if membership.contest_id == EmptyValues.EMPTY_INT else membership.contest_id,
                'goes_for_coalition': membership.goes_for_coalition,
                'membership_type': Catalogues.MEMBERSHIP_TYPES[membership.membership_type],
                'goes_for_reelection': membership.goes_for_reelection,
                'start_date': "" if membership.start_date.strftime('%Y-%m-%d') == date.fromisoformat(EmptyValues.EMPTY_DATE).strftime('%Y-%m-%d') else membership.start_date.strftime('%Y-%m-%d'),
                'end_date': "" if membership.end_date.strftime('%Y-%m-%d') == date.fromisoformat(EmptyValues.EMPTY_DATE).strftime('%Y-%m-%d') else membership.end_date.strftime('%Y-%m-%d'),
                'is_substitute': membership.is_substitute,
                'parent_membership_id': "" if membership.parent_membership_id == EmptyValues.EMPTY_INT else membership.parent_membership_id,
                'changed_from_substitute': "" if membership.changed_from_substitute == EmptyValues.EMPTY_INT else membership.changed_from_substitute,
                'date_changed_from_substitute': "" if membership.date_changed_from_substitute.strftime('%Y-%m-%d') == date.fromisoformat(EmptyValues.EMPTY_DATE).strftime('%Y-%m-%d') else membership.date_changed_from_substitute.strftime('%Y-%m-%d'),
                'source_urls': Url.get_membership_source_urls(membership.membership_id)
            }
            result.append(obj)
        return result

    def delete(self):
        db.session.delete(self)
        db.session.commit()
