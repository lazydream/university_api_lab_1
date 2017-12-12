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
import TeachersCardTemplate from './TeachersCardTemplate'

class TeachersTable extends Component {
    constructor(props) {
        super(props);
        this.state = {
            teachers: []
        }
    }
    componentWillMount() {
        const url = `/api/teachers`;
        fetch(url).then(res => res.json())
            .then(teachers => {
                this.setState({
                    teachers
                })
            })
    }

    render() {
        const {teachers} = this.state;
        return (
            <TeachersCardTemplate subtitle="Таблица">
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
                            <TableHeaderColumn>Код кафедры</TableHeaderColumn>
                        </TableRow>
                    </TableHeader>
                    <TableBody
                        displayRowCheckbox={false}
                    >
                        {teachers.map(teacher => {
                            return (
                                <TableRow>
                                    <TableRowColumn>{teacher.id}</TableRowColumn>
                                    <TableRowColumn>{teacher.name}</TableRowColumn>
                                    <TableRowColumn>{teacher.gender}</TableRowColumn>
                                    <TableRowColumn>{teacher.birth_date}</TableRowColumn>
                                    <TableRowColumn>{teacher.phone_number}</TableRowColumn>
                                    <TableRowColumn>{teacher.departament_id}</TableRowColumn>
                                </TableRow>
                            )
                        })}
                    </TableBody>
                </Table>
            </TeachersCardTemplate>
        )
    }
}


export default TeachersTable;