# Write a function get_top_players(variant, count) that fetches the top count players for a given chess variant (e.g. "bullet", "blitz", "rapid").
# Write a function get_player_profile(username) that fetches a single player's public profile.
# Using those, write build_leaderboard(variant, count) that returns a clean list of dicts ranked by rating, each with rank, username, and rating.

import requests
import json

def get_book_info(title):
    # return dict of title, author, year 
    response = requests.get(f"https://openlibrary.org/search.json?title={title}")
    d = response.json()
    result = {
        "author": d["docs"][0]["author_name"][0] ,
        "title": d["docs"][0]["title"],
        "year": d["docs"][0]["first_publish_year"]
    }
    return result  
    # return response.json()

def get_top_players(variant, count):
    response = requests.get(f"https://lichess.org/api/player/top/{count}/{variant}")
    # top_players = list(json.dumps(response))[:count] # json.dumps(..) makes it a string
    top_players = response.json()
    return top_players


def get_player_profile(username):
    profile = requests.get(f"https://lichess.org/api/user/{username}")
    return profile.json()

def build_leaderboard(variant, count):
    players = get_top_players(variant, count)
    # print(players)
    l = []
    for idx, player in enumerate(players["users"]):
        # print("HERE", idx, player, "\n")
        d = {
            "rank": idx,
            "username": player["username"],
            "rating": player["perfs"][variant]
        }
        l.append(d)
        
    return l
    # return sorted(result.items(), key=lambda x:x[0])

def get_player_rating(username, variant):
    player = get_player_profile(username)
    if player == None:
        return None

    else:
        rating = player["perfs"][variant]["rating"]
        return rating

def compare_players(username1, username2, variant):
    player1 = get_player_rating(username1, variant)
    player2 = get_player_rating(username2, variant)

    try:
        if player1 == player2:
            return "tie"
        return username1 if player1 >= player2 else username2
    except TypeError:
        return "Invalid player"

if __name__ == "__main__":
    print(get_book_info("the great gatsby"))
    # print(get_top_players("bullet", 10))
    # print(get_player_profile("magnuscarlsen"))
    # print(build_leaderboard("bullet", 10))
    # print(get_player_rating("magnuscarlsen", "bullet"))
    # print(compare_players("magnuscarlsen", "magnuscarlsen", "bullet"))








'''
import random

reset_tokens = {}

def generate_reset_token(email):
    token = str(random.randint(1000, 9999))
    reset_tokens[token] = email
    return token

def verify_reset_token(token, email):
    if token in reset_tokens:
        if reset_tokens[token] == email:
            del reset_tokens[token]
            return True
    return False

# Test 1 — Happy path
token = generate_reset_token("alice@example.com")
result = verify_reset_token(token, "alice@example.com")
print(result)  # Should return True

# Test 2 — Wrong email
token = generate_reset_token("alice@example.com")
result = verify_reset_token(token, "bob@example.com")
print(result)  # Should return False

# Test 3 — Token used twice (should be single use)
token = generate_reset_token("alice@example.com")
verify_reset_token(token, "alice@example.com")
result = verify_reset_token(token, "alice@example.com")
print(result)  # Should return False — token already consumed

# Test 4 — Token collision (security issue)
tokens = [generate_reset_token(f"user{i}@example.com") for i in range(1000)]
print(len(set(tokens)))  # How many are unique? Should be 1000 — are they?

# Test 5 — Expired token (missing feature)
import time
token = generate_reset_token("alice@example.com")
time.sleep(2)
result = verify_reset_token(token, "alice@example.com")
print(result)  # Should this still be valid after 10 mins? 1 hour? '''

'''
call_count = 0

import requests

def get_user_profile(user_id):
    global call_count
    call_count += 1
    response = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
    return response.json()

def get_multiple_profiles(user_ids):
    results = {}
    for user_id in set(user_ids):
        results[user_id] = get_user_profile(user_id)
    return results

result = get_multiple_profiles(["1", "1", "1"])
print(call_count)  # Should print 3 — redundant calls

# Test 1 — Basic single fetch
# print(get_multiple_profiles(["1", "1", "1"]))   # duplicate test
# sprint(get_multiple_profiles(["1", "2", "3"]))  # unique test

# Test 1 — Basic single fetch
# result = get_multiple_profiles(["user_1"])
# print(result)  # Should return {"user_1": {...}}

# Test 2 — Duplicate user_ids in input
# eesult = get_multiple_profiles(["user_1", "user_1", "user_1"])
# print(result)  # Should only make 1 network call, not 3

# Test 3 — Empty input
# result = get_multiple_profiles([])
# print(result)  # Should return {}

# Test 4 — Large list with repeats (performance)
# ids = [f"user_{i % 5}" for i in range(1000)]  # only 5 unique users
# result = get_multiple_profiles(ids)
# print(len(result))  # Should be 5, and only 5 network calls made'''


'''
def create_payment(user_id, amount, idempotency_key): # "user_1", 100, "key_123"
    if idempotency_key in idempotency_store:
        stored = idempotency_store[idempotency_key]

        if stored["user_id"] != user_id or stored["amount"] != amount:
            raise ValueError("Idempotency key reused with different payload")

        return payments[stored["payment_id"]]
    
    payment_id = f"pay_{len(payments.keys()) + 1}"
    payment = {
        "payment_id": payment_id,
        "user_id": user_id,
        "amount": amount,
        "status": "processed"
    }

    print(payment_id)
    print(payments)
    payments[payment_id] = payment
    idempotency_store[idempotency_key] = payment_id # "key_123": "user_1"

    return payment



payments = {}
idempotency_store = {}

# result = create_payment("user_1", 100, "key_123")
# print(result)

# first = create_payment("user_1", 100, "key_123")
# second = create_payment("user_1", 100, "key_123")

first = create_payment("user_1", 100, "key_123")
second = create_payment("user_1", 999, "key_123")

print("First:", first)
print("Second:", second)
print(payments)


def get_candidates(candidates, limit=2, cursor=None):
    candidates = sorted(candidates, key=lambda c: (c["created_at"], c["id"]))

    start = 0
    if cursor is not None:
        for i, candidate in enumerate(candidates):
            if candidate["created_at"] >= cursor:
                start = i
                break

    page = candidates[start:start + limit]
    next_cursor = None

    if len(page) == limit:
        next_cursor = page[-1]["created_at"]

    return {
        "results": page,
        "next_cursor": next_cursor
    }

candidates = [
    {"id": 1, "created_at": 100},
    {"id": 2, "created_at": 100},
    {"id": 3, "created_at": 101},
    {"id": 4, "created_at": 102},
]

result = get_candidates(candidates, limit=2)
print(result)
# expected "next_cursor": (100, 2)  


VALID_TRANSITIONS = {
    "applied": {"screened", "rejected"},
    "screened": {"interviewed", "rejected"},
    "interviewed": {"offered", "rejected"},
    "offered": {"hired", "rejected"},
    "hired": set(),
    "rejected": set(),
}

def update_status(application, new_status):
    current_status = application["status"]

    # edge cases
    if current_status == None:
        raise ValueError(f"Unknown current status: {current_status}")

    if new_status in VALID_TRANSITIONS[current_status]:
        application["status"] = new_status
        if application["history"]:
            application["history"].append({
                "from": current_status,
                "to": new_status
            })
            return application

    raise ValueError("Invalid status transition")


# Test Case 1 
application = {
    "status": "applied",
    "history": []
}

result = update_status(application, "screened")

# Test Case 2
application2 = {
    "status": "applied",
    "history": []
}

application3 = {
    "status": "rejected",
    "history": []
}

print(update_status(application3, "screened"))



active_sessions = {}

def create_session(user_id, token):
    print("Line 4:", active_sessions)
    
    if user_id in active_sessions.keys():
        raise ValueError("Session already exists")
    
    active_sessions["user_id"] = token
    return token

def get_session(user_id):
    if user_id in active_sessions.keys():
        return active_sessions[user_id]
    return None


result = create_session("user_1", "token_abc")
# print(result)  # Should return the token
# create_session("user_1", "token_abc")
# create_session("user_1", "token_xyz")  # Should raise ValueError

# create_session("user_1", "token_abc")
create_session("user_1", "token_xyz")  # Should NOT raise
print(get_session("user_3"))'''