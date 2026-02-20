# MongoDB In-Class Activity

## Setup (5 minutes)

1. Clone this repo
   ```bash
   git clone <repo-url>
   cd mongo-activity
   ```

2. Create and activate a virtual environment
   
   **macOS/Linux:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
   
   **Windows:**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. Start the database:
   ```bash
   docker-compose up -d
   ```

5. Verify it's running:
   ```bash
   docker ps
   ```

You now have a MongoDB database with two collections:
- `instructors` — 8 instructors with name, department, email, years_teaching
- `courses` — 18 courses with code, title, instructor_id, credits, enrollment, level, tags

## Connect with Python

```python
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['university']
courses = db['courses']
instructors = db['instructors']
```

## Exercises

### Part 1: Basic Queries

1. **Count all courses**
   ```python
   courses.count_documents({})
   ```

2. **Find all graduate-level courses**
   ```python
   for c in courses.find({'level': 'graduate'}):
       print(c['code'], c['title'])
   ```

3. **Find courses with enrollment over 100**

4. **Find all instructors in Computer Science**

5. **Find courses worth 4 credits**

### Part 2: Query Operators

6. **Find courses with enrollment between 50 and 100**
   ```python
   courses.find({'enrollment': {'$gte': 50, '$lte': 100}})
   ```

7. **Find instructors with 10+ years teaching experience**

8. **Find courses that are NOT undergraduate level**

9. **Find courses with "programming" in their tags**
   ```python
   courses.find({'tags': 'programming'})
   ```

### Part 3: Cross-Collection Queries

10. **Find all courses taught by a specific instructor**
    ```python
    # First find the instructor
    instructor = instructors.find_one({'name': 'Alice Chen'})
    
    # Then find their courses
    for c in courses.find({'instructor_id': instructor['_id']}):
        print(c['title'])
    ```

11. **For each course, print the course title AND instructor name**

12. **Find the instructor who teaches the course with highest enrollment**

13. **List all departments and how many courses each offers**

### Part 4: Aggregation Pipeline

14. **Average enrollment by level (undergraduate vs graduate)**
    ```python
    pipeline = [
        {'$group': {'_id': '$level', 'avg_enrollment': {'$avg': '$enrollment'}}}
    ]
    for result in courses.aggregate(pipeline):
        print(result)
    ```

15. **Total enrollment per department** (hint: need to join with instructors)

16. **Find the instructor teaching the most courses**

### Part 5: Creative Exploration

17. Come up with your own interesting question about this data and write the query to answer it.

## Cleanup

```bash
docker-compose down
deactivate
```

## Data Schema Reference

### instructors
```json
{
  "_id": 1,
  "name": "Alice Chen",
  "department": "Computer Science",
  "email": "achen@university.edu",
  "years_teaching": 12
}
```

### courses
```json
{
  "code": "CS101",
  "title": "Introduction to Programming",
  "instructor_id": 1,
  "credits": 3,
  "enrollment": 120,
  "level": "undergraduate",
  "tags": ["programming", "python", "beginner"]
}
```
