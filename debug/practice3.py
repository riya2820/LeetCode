from collections import defaultdict
import threading
import requests
import time


def mystery(nums):
    stack = []
    result = [-1] * len(nums)
    print("Result", result)
    
    for i, num in enumerate(nums):
        print(f"Nums={nums}, i={i}, num={num}")
        while stack and nums[stack[-1]] < num:
            idx = stack.pop()
            print(f"Pop element:{idx}")
            result[idx] = num
            print("new result", result)
        stack.append(i)
        print(f"Stack: {stack}")
    
    return result

# What does this return for:
nums = [2, 1, 5, 3, 6, 4]
print(mystery(nums))

'''
def process(data):
    result = defaultdict(list)
    for item in data:
        key = item["type"]
        result[key].append(item["value"])
    
    for key in result:
        result[key] = sum(result[key]) / len(result[key])
    
    return result

data = [
    {"type": "a", "value": 10},
    {"type": "b", "value": 20},
    {"type": "a", "value": 30},
    {"type": "b", "value": 40},
    {"type": "a", "value": 50},
]
print(process(data))

def binary_search(arr, target):
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1

def merge_counts(events):
    # counts = {}
    counts = defaultdict(int)
    for event in events:
        event_type = event["type"]
        counts[event_type] += 1
        # if event_type in counts:
        #     counts[event_type] += 1
        # else:
        #    counts[event_type] = 1
    return counts

events = [
    {"type": "click"},
    {"type": "view"},
    {"type": "click"},
]
print(merge_counts(events))

# [
#   {"id": 1, "name": "Riya", "order_count": 2},
#    {"id": 2, "name": "Sam", "order_count": 1},
#  ]
def attach_order_counts(users, orders):
    result = []
    for user in users:
        count = 0
        if order[user["user_id"]]:
            count 

        for order in orders:
            if order["user_id"] == user["id"]:
                count += 1
        result.append({
            "id": user["id"],
            "name": user["name"],
            "order_count": count
        })
    return list(result)


users = [
    {"id": 1, "name": "Riya"},
    {"id": 2, "name": "Sam"},
]

orders = [
    {"id": 101, "user_id": 1},
    {"id": 102, "user_id": 1},
    {"id": 103, "user_id": 2},
]
print("orders:", attach_order_counts(users, orders))


# def get_profile(user_id, cache={}):
def get_profile(user_id, cache=None): # want to do this set none as default instead of authorize it as empty
    if cache is None:
        cache = {}
    if user_id in cache:
        return cache[user_id]

    profile = {"id": user_id, "name": f"user-{user_id}"}
    cache[user_id] = profile
    return profile



def allow_request(user_id, requests):
    now = time.time()
    if user_id not in requests:
        requests[user_id] = []

    recent = []
    for ts in requests[user_id]:
        if now - ts < 10:
            recent.append(ts)

    if len(recent) >= 3:
        requests[user_id] = recent
        return False

    recent.append(now)
    requests[user_id] = recent
    return True


def timer(func):
    def wrapper(*args, **kwargs):
        # your code here
        pass
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    return "done"

print("Output:", slow_function())  # should print: "slow_function took 1.00s"



def has_duplicate_usernames(usernames):
    for i in range(len(usernames)): # O(n^2)
        for j in range(i + 1, len(usernames)):
            if usernames[i] == usernames[j]:
                return True
    return False
    # instead O(n)
    # return len(usernames) == len(set(usernames))
usernames = ["ri", "ya", "jo"]
print(has_duplicate_usernames(usernames))


def find_common(list1, list2):
    common = []
    set2 = set(list2)
    for item in list1: # O(n) instead of original O(1), set lookup is O(1)
        if item in set2:
            common.append(item)
    return common

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
print(find_common(list1, list2))


counter = 0

def increment():
    global counter
    for _ in range(100_000):
        counter += 1

threads = [threading.Thread(target=increment) for _ in range(5)]
for t in threads: t.start()
for t in threads: t.join()

print("Counter:", counter)  # Expected: 500_000. Actual?

def subarraySum(nums, k):
    l,r = 0, 1
    total = 0
    paths = []
      
    while l < len(nums)-1:
        total += nums[l] 
        while total < k and r < len(nums): 
            total += nums[r] 
            r += 1 
        paths.append(r-l) 
        l += 1
        r = l+1 # becoming O(N^2)
        total = 0 
        
    return min(paths) if paths else 0


nums = [2, 3, 1, 2, 4, 3]
k = 7
print(subarraySum(nums, k))

nums = [2, 3, 1, 2, 4]
k = 7
print(subarraySum(nums, k))
# Output: 2  (subarray [4,3])

# Design a Least Recently Used (LRU) cache with capacity k. 
# Both get(key) and put(key, value) must run in O(1) time. Walk through the data structure(s) you'd use and why.

# get(key) → return value or -1
# put(key, value) → insert; if over capacity, evict LRU
# Both must be O(1)


def get_weather(city):
    try:
        response = requests.get(f"https://api.weather.com/{city}", timeout=5)
        response.raise_for_status()
        return response.json()
    
    except requests.exceptions.Timeout as e:
        if attempt == retries - 1:
            return "Request timed out after retries"
        except requests.exceptions.HTTPError as e:
                return f"HTTP error: {e}"
        except requests.exceptions.RequestException as e:
            return f"Request failed: {e}"

print(get_weather("Mumbai"))  

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key) 
        return self.cache[key]


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update the value and move the key to the end (MRU position)
            self.cache[key] = value
            self.cache.move_to_end(key)
        else:
            # Add the new key-value pair
            self.cache[key] = value
            # Check if capacity is exceeded
            if len(self.cache) > self.capacity:
                # Remove the least recently used item (first item)
                self.cache.popitem(last=False)

k = 5
A = LRUCache()
print(lru(k)) 


def find_duplicates(nums):
    seen = set()
    duplicates = set()

    for n in nums:
        if n in seen: 
            duplicates.add(n)
        seen.add(n)
    return duplicates


nums = [2,2,3,4]
print(find_duplicates(nums))

 

from collections import defaultdict

def firstNonRepeating(s):
    d = defaultdict(int)

    for char in s:
        d[char] += 1

    for k, v in d.items():
        if v == 1:
            return k

    return None
     
     
s = "aabccbd"
print("Result:", firstNonRepeating(s))
# Expected output: "d"


def get_user_orders(user_id):
    query = f"SELECT * FROM orders WHERE user_id = {user_id}"
    return db.execute(query)

# Called like this:
# get_user_orders("1 OR 1=1")
print(get_user_orders("1"))




def get_page(items, cursor=None, limit=2):
    start = 0
    if cursor is not None:
        for i, item in enumerate(items):
            print(i,item)
            if item["created_at"] > cursor:
                start = i
                break
    page = items[start:start+limit] # page = items[0:2]
    # next_cursor = page[-1]["created_at"] if len(page) == limit else None
    next_cursor = page[-1]["created_at"]+1 if page else start # 100 
    return page, next_cursor


items = [
    {"id": 1, "created_at": 100},
    {"id": 2, "created_at": 100},
    {"id": 3, "created_at": 101},
    {"id": 4, "created_at": 102},
]

page1, cursor1 = get_page(items, limit=2)
page2, cursor2 = get_page(items, cursor=cursor1, limit=2)

print("page1", page1)
print("cursor1", cursor1)
print("page2", page2)
print("cursor2", cursor2)

'''