#!/usr/bin/python3
"""Script de test pour task_04_flask.py"""
import requests
import json

BASE_URL = "http://localhost:5000"

print("=" * 60)
print("Tests pour Task 4: Flask API")
print("=" * 60)

# Test 1: Root endpoint
print("\n[Test 1] GET /")
response = requests.get(f"{BASE_URL}/")
print(f"Status: {response.status_code}")
print(f"Response: {response.text}")

# Test 2: Status endpoint
print("\n[Test 2] GET /status")
response = requests.get(f"{BASE_URL}/status")
print(f"Status: {response.status_code}")
print(f"Response: {response.text}")

# Test 3: Add user
print("\n[Test 3] POST /add_user")
user_data = {
    "username": "alice",
    "name": "Alice",
    "age": 25,
    "city": "Paris"
}
response = requests.post(
    f"{BASE_URL}/add_user",
    json=user_data,
    headers={"Content-Type": "application/json"}
)
print(f"Status: {response.status_code}")
print(f"Response: {json.dumps(response.json(), indent=2)}")

# Test 4: Get user
print("\n[Test 4] GET /users/alice")
response = requests.get(f"{BASE_URL}/users/alice")
print(f"Status: {response.status_code}")
print(f"Response: {json.dumps(response.json(), indent=2)}")

# Test 5: Get all usernames
print("\n[Test 5] GET /data")
response = requests.get(f"{BASE_URL}/data")
print(f"Status: {response.status_code}")
print(f"Response: {response.json()}")

# Test 6: User not found
print("\n[Test 6] GET /users/nonexistent")
response = requests.get(f"{BASE_URL}/users/nonexistent")
print(f"Status: {response.status_code}")
print(f"Response: {json.dumps(response.json(), indent=2)}")

# Test 7: Username required
print("\n[Test 7] POST /add_user (no username)")
response = requests.post(
    f"{BASE_URL}/add_user",
    json={"name": "Bob"},
    headers={"Content-Type": "application/json"}
)
print(f"Status: {response.status_code}")
print(f"Response: {json.dumps(response.json(), indent=2)}")

# Test 8: Duplicate username
print("\n[Test 8] POST /add_user (duplicate)")
response = requests.post(
    f"{BASE_URL}/add_user",
    json=user_data,
    headers={"Content-Type": "application/json"}
)
print(f"Status: {response.status_code}")
print(f"Response: {json.dumps(response.json(), indent=2)}")

# Test 9: Invalid JSON
print("\n[Test 9] POST /add_user (invalid JSON)")
response = requests.post(
    f"{BASE_URL}/add_user",
    data="not json",
    headers={"Content-Type": "application/json"}
)
print(f"Status: {response.status_code}")
print(f"Response: {json.dumps(response.json(), indent=2)}")

print("\n" + "=" * 60)
print("Tests terminés")
print("=" * 60)
