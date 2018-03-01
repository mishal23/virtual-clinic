import logging
from datetime import datetime
from server.models import Action

console_logger = logging.getLogger(__name__)

def log(type, description, account):
    action = Action(
        type = type,
        timePerformed = datetime.now(),
        description = description,
        account = account,
    )
    action.save()

def debug(message):
    console_logger.error(message)