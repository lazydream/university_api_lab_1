from flask import url_for


def format_departaments(departaments):
    for departament in departaments:
        departament['links'] = [
            {
                'rel': 'groups',
                'href': url_for('groups_views.groups', departament_id=departament['id'])
            },
            {
                'rel': 'teachers',
                'href': url_for('teachers_views.teachers', departament_id=departament['id'])
            }
        ]
    return departaments


def format_teachers(teachers, teachers_courses):
    res = []
    ids = []
    for teacher in teachers:
        if teacher['id'] not in ids:
            ids.append(teacher['id'])
            teacher['links'] = [
                {
                    'rel': 'course',
                    'href': url_for('courses_views.course', course_id=teacher['course_id'])
                }
            ]
            res.append(teacher)
        else:
            tchr = next((tchr for tchr in res if tchr['id'] == teacher['id']))
            tchr['links'].append({
                'rel': 'course',
                'href': url_for('courses_views.course', course_id=teacher['course_id'])
            })
    return teachers


def format_groups(groups):
    for group in groups:
        group['links'] = [{
            'rel': 'students',
            'href': url_for('students_views.students', departament_id=group['departament_id'], group_id=group['id'])
        }]
    return groups
