"""
MongoDB In-Class Activity
University Course Database

Run this file to test your connection, then complete the exercises below.
"""

from pymongo import MongoClient

# Connect to the database
client = MongoClient('localhost', 27017)
db = client['university']
courses = db['courses']
instructors = db['instructors']

# Test connection
print(f"Connected! Found {courses.count_documents({})} courses and {instructors.count_documents({})} instructors.\n")

# Example: Print all course codes
print("All courses:")
for c in courses.find():
    print(f"  {c['code']}: {c['title']}")

print("\n" + "="*50)
print("YOUR EXERCISES BELOW")
print("="*50 + "\n")

# Exercise 1: Find all graduate-level courses
# Your code here


# Exercise 2: Find courses with enrollment over 100
# Your code here


# Exercise 3: Find all instructors in Computer Science
# Your code here


# Exercise 4: Find courses with "programming" in their tags
# Your code here


# Exercise 5: For each course, print the course title AND instructor name
# Hint: You'll need to query both collections
# Your code here
