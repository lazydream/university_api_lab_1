from datetime import datetime

from flask import url_for


def format_departaments(departaments, groups_rel, teachers_rel):
    for rel in groups_rel:
        d = next((d for d in departaments if d['id'] == rel['id']))
        d['links'] = [
            {
                'rel': 'groups',
                'href': url_for('groups_views.groups', departament_id=d['id'])
            }
        ]

    for rel in teachers_rel:
        d = next((d for d in departaments if d['id'] == rel['id']))
        if not d['links']:
            d['links'] = []
        d['links'].append({
                'rel': 'teachers',
                'href': url_for('teachers_views.teachers', departament_id=d['id'])
            })
    return departaments


def format_teachers(teachers, teachers_courses):
    for rel in teachers_courses:
        teacher = next((tchr for tchr in teachers if rel['id'] == tchr['id']))
        teacher['links'] = [
            {
                'rel': 'course',
                'href': url_for('courses_views.course', course_id=rel['course_id'])
            }
        ]
    return teachers


def format_groups(groups):
    for group in groups:
        group['links'] = [{
            'rel': 'students',
            'href': url_for('students_views.students', departament_id=group['departament_id'], group_id=group['id'])
        }]
    return groups


def calculate_age(birth_date):
    date_now = datetime.now()
    age = date_now.year - birth_date.year
    if date_now.month < birth_date.month and date_now.day < birth_date.day:
        age -= 1
    return age
