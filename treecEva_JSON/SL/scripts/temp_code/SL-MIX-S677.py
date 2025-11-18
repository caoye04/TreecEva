import re
from dataclasses import dataclass
from enum import Enum

class DocumentState(Enum):
    INIT = 1
    PARSED = 2
    SECURITY_CHECKED = 3
    ACCESS_GRANTED = 4

def tokenize(text):
    return re.findall(r'\b\w+\b', text)

def evaluate_security(tokens):
    has_confidential = any(token.lower() == 'confidential' for token in tokens)
    has_public = any(token.lower() == 'public' for token in tokens)
    return has_confidential and not has_public

def calculate_access(base_clearance, is_secure, has_override):
    if is_secure and not has_override:
        return 0
    elif is_secure and has_override:
        return base_clearance - 1
    else:
        return base_clearance + 2

@dataclass
class DocumentMetadata:
    content: str
    clearance_level: int
    override_code: bool = False

metadata = DocumentMetadata(
    content="This confidential document contains sensitive operational data",
    clearance_level=3,
    override_code=True
)

state = DocumentState.INIT
access_level = 0

while state != DocumentState.ACCESS_GRANTED:
    if state == DocumentState.INIT:
        tokens = tokenize(metadata.content)
        state = DocumentState.PARSED
    elif state == DocumentState.PARSED:
        is_secure = evaluate_security(tokens)
        state = DocumentState.SECURITY_CHECKED
    elif state == DocumentState.SECURITY_CHECKED:
        access_level = calculate_access(metadata.clearance_level, is_secure, metadata.override_code)
        state = DocumentState.ACCESS_GRANTED

print(f"Result: {access_level}")