from flask import Flask, request, jsonify
from datetime import datetime
from typing import List, Dict
import uuid

app = Flask(__name__)

# ---------- ENUMS ----------
class CommitmentType:
    CLASS = "CLASS"
    WORK = "WORK"
    SOCIAL = "SOCIAL"
    EXERCISE = "EXERCISE"
    OTHER = "OTHER"

class EventType:
    PREP = "PREP"
    COMMITMENT = "COMMITMENT"
    MEAL = "MEAL"
    REST = "REST"
    REMINDER = "REMINDER"

# ---------- MODELS ----------
class Commitment:
    def __init__(self, title, location, start_time, end_time, commitment_type):
        self.id = str(uuid.uuid4())
        self.title = title
        self.location = location
        self.start_time = start_time
        self.end_time = end_time
        self.type = commitment_type

class Schedule:
    def __init__(self):
        self.commitments: List[Commitment] = []

    def addCommitment(self, commitment: Commitment):
        self.commitments.append(commitment)

    def getCommitmentsForDay(self, date: str) -> List[Commitment]:
        return [c for c in self.commitments if c.start_time.startswith(date)]

class Checklist:
    def __init__(self):
        self.items: Dict[str, List[str]] = {}

    def addItems(self, commitment_type: str, items: List[str]):
        self.items[commitment_type] = items

    def getItems(self, commitment_type: str) -> List[str]:
        return self.items.get(commitment_type, [])

class PlannedEvent:
    def __init__(self, title, start_time, end_time, event_type, prep_items=None):
        self.title = title
        self.start_time = start_time
        self.end_time = end_time
        self.type = event_type
        self.preparationItems = prep_items or []

class DailyPlan:
    def __init__(self, date: str):
        self.date = date
        self.plannedEvents: List[PlannedEvent] = []

    def generate(self, user):
        commitments = user.schedule.getCommitmentsForDay(self.date)
        for c in commitments:
            prep_items = user.getChecklistFor(c.type)
            event = PlannedEvent(
                title=c.title,
                start_time=c.start_time,
                end_time=c.end_time,
                event_type=EventType.COMMITMENT,
                prep_items=prep_items
            )
            self.plannedEvents.append(event)

    def to_dict(self):
        return {
            "date": self.date,
            "plannedEvents": [
                {
                    "title": e.title,
                    "startTime": e.start_time,
                    "endTime": e.end_time,
                    "type": e.type,
                    "prepItems": e.preparationItems
                }
                for e in self.plannedEvents
            ]
        }

class User:
    def __init__(self, name, email):
        self.id = str(uuid.uuid4())
        self.name = name
        self.email = email
        self.schedule = Schedule()
        self.checklist = Checklist()

    def addCommitment(self, commitment: Commitment):
        self.schedule.addCommitment(commitment)

    def getChecklistFor(self, commitment_type: str) -> List[str]:
        return self.checklist.getItems(commitment_type)

    def getDailyPlan(self, date: str) -> DailyPlan:
        plan = DailyPlan(date)
        plan.generate(self)
        return plan

# ---------- MOCK USER ----------
test_user = User("Alex", "alex@example.com")

# Add a commitment (meeting a friend at 5:30pm)
test_user.addCommitment(Commitment(
    title="Meet Friend at Reading Terminal",
    location="Center City",
    start_time="2025-05-06T17:30",
    end_time="2025-05-06T19:00",
    commitment_type=CommitmentType.SOCIAL
))

# Add a checklist for SOCIAL events
test_user.checklist.addItems(CommitmentType.SOCIAL, [
    "Pack water bottle",
    "Grab keys",
    "Wear makeup"
])

# ---------- API ----------
@app.route("/plan/<date>", methods=["GET"])
def get_plan(date):
    """
    GET /plan/2025-05-06
    """
    plan = test_user.getDailyPlan(date)
    return jsonify(plan.to_dict())

# ---------- MAIN ----------
if __name__ == "__main__":
    app.run(debug=True, port=5001)
