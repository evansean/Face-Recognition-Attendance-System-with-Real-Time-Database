import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import creds

firebase_admin.initialize_app(creds.cred,{
    'databaseURL': 'https://faceattendancerealtime-70b36-default-rtdb.asia-southeast1.firebasedatabase.app/'
})


ref = db.reference('Students')

data = {
    '666666':
        {
            "name": "Evan Sean Sainani",
            "major": "Computer Science",
            "starting_year": 2017,
            "total_attendance": 6,
            "standing": "G",
            "year":4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    '555666':
        {
            "name": "Ian Joshua Sainani",
            "major": "Gender Studies",
            "starting_year": 2017,
            "total_attendance": 6,
            "standing": "G",
            "year":4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    '696969':
        {
            "name": "Ian Richard D'silva",
            "major": "Catechism",
            "starting_year": 2017,
            "total_attendance": 6,
            "standing": "G",
            "year":4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    '071326':
        {
            "name": "Yeow Loon Guek",
            "major": "Catechism",
            "starting_year": 2017,
            "total_attendance": 6,
            "standing": "G",
            "year":4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    '321654':
        {
            "name": "Murtaza Hassan",
            "major": "Robotics",
            "starting_year": 2017,
            "total_attendance": 6,
            "standing": "G",
            "year":4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    '852741':
        {
            "name": "Emily Blunt",
            "major": "Economics",
            "starting_year": 2018,
            "total_attendance": 12,
            "standing": "B",
            "year":2,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    '963852':
        {
            "name": "Elon Musk",
            "major": "Physics",
            "starting_year": 2020,
            "total_attendance": 6,
            "standing": "G",
            "year":2,
            "last_attendance_time": "2022-12-11 00:54:34"
        }    
}

for key, value in data.items():
    ref.child(key).set(value)