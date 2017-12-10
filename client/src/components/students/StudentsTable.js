import React, {Component} from 'react';
import {
    Table,
    TableBody,
    TableHeader,
    TableHeaderColumn,
    TableRow,
    TableRowColumn,
} from 'material-ui/Table';
import RaisedButton from 'material-ui/RaisedButton';
import StudentsCardTemplate from './StudentsCardTemplate'

class StudentsTable extends Component {
    constructor(props) {
        super(props);
        this.state = {
            students: []
        }
    }
    componentWillMount() {
        const url = `/api/students`;
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
            <StudentsCardTemplate subtitle="Таблица">
                <Table
                    selectable={false}
                >
                    <TableHeader
                        adjustForCheckbox={false}
                        displaySelectAll={false}
                    >
                        <TableRow>
                            <TableHeaderColumn>Код</TableHeaderColumn>
                            <TableHeaderColumn>ФИО</TableHeaderColumn>
                            <TableHeaderColumn>Пол</TableHeaderColumn>
                            <TableHeaderColumn>Дата рождения</TableHeaderColumn>
                            <TableHeaderColumn>Телефон</TableHeaderColumn>
                            <TableHeaderColumn>Код группы</TableHeaderColumn>
                            <TableHeaderColumn>Отчет</TableHeaderColumn>
                        </TableRow>
                    </TableHeader>
                    <TableBody
                        displayRowCheckbox={false}
                    >
                        {students.map(student => {
                            return (
                                <TableRow>
                                    <TableRowColumn>{student.id}</TableRowColumn>
                                    <TableRowColumn>{student.name}</TableRowColumn>
                                    <TableRowColumn>{student.gender}</TableRowColumn>
                                    <TableRowColumn>{student.birth_date}</TableRowColumn>
                                    <TableRowColumn>{student.phone_number}</TableRowColumn>
                                    <TableRowColumn>{student.group_id}</TableRowColumn>
                                    <TableRowColumn>
                                        <RaisedButton href={`/api/students/${student.id}/report`} label="Получить отчет"/>
                                    </TableRowColumn>
                                </TableRow>
                            )
                        })}
                    </TableBody>
                </Table>
            </StudentsCardTemplate>
        )
    }
}


export default StudentsTable;