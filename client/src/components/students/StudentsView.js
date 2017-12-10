import React, {Component} from 'react';
import {
    Table,
    TableBody,
    TableHeader,
    TableHeaderColumn,
    TableRow,
    TableRowColumn,
} from 'material-ui/Table';
import StudentsCardTemplate from './StudentsCardTemplate'

class StudentsView extends Component {
    constructor(props) {
        super(props);
        this.state = {
            students: []
        }
    }
    componentWillMount() {
        const url = `/api/students/view`;
        fetch(url).then(res => res.json())
            .then(students => {
                this.setState({
                    students
                })
            })
    }

    render() {
        const {students} = this.state;
        return (
            <StudentsCardTemplate subtitle="Представление">
                <Table
                    selectable={false}
                >
                    <TableHeader
                        adjustForCheckbox={false}
                        displaySelectAll={false}
                    >
                        <TableRow>
                            <TableHeaderColumn>Код</TableHeaderColumn>
                            <TableHeaderColumn>Группа</TableHeaderColumn>
                            <TableHeaderColumn>ФИО</TableHeaderColumn>
                            <TableHeaderColumn>Курс</TableHeaderColumn>
                            <TableHeaderColumn>Пол</TableHeaderColumn>
                            <TableHeaderColumn>Возраст</TableHeaderColumn>
                            <TableHeaderColumn>Телефон</TableHeaderColumn>
                            <TableHeaderColumn>Кафедра</TableHeaderColumn>
                        </TableRow>
                    </TableHeader>
                    <TableBody
                        displayRowCheckbox={false}
                    >
                        {students.map(student => {
                            return (
                                <TableRow>
                                    <TableRowColumn>{student.id}</TableRowColumn>
                                    <TableRowColumn>{student.group_name}</TableRowColumn>
                                    <TableRowColumn>{student.name}</TableRowColumn>
                                    <TableRowColumn>{student.course || '-'}</TableRowColumn>
                                    <TableRowColumn>{student.gender}</TableRowColumn>
                                    <TableRowColumn>{student.age}</TableRowColumn>
                                    <TableRowColumn>+{student.phone_number}</TableRowColumn>
                                    <TableRowColumn>{student.departament_name}</TableRowColumn>
                                </TableRow>
                            )
                        })}
                    </TableBody>
                </Table>

            </StudentsCardTemplate>
        )
    }
}


export default StudentsView;