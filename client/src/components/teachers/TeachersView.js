import React, {Component} from 'react';
import {
    Table,
    TableBody,
    TableHeader,
    TableHeaderColumn,
    TableRow,
    TableRowColumn,
} from 'material-ui/Table';
import TeachersCardTemplate from './TeachersCardTemplate'

class TeachersView extends Component {
    constructor(props) {
        super(props);
        this.state = {
            teachers: []
        }
    }
    componentWillMount() {
        const url = `/api/teachers/view`;
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
            <TeachersCardTemplate subtitle="Представление">
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
                            <TableHeaderColumn>Возраст</TableHeaderColumn>
                            <TableHeaderColumn>Телефон</TableHeaderColumn>
                            <TableHeaderColumn>Кафедра</TableHeaderColumn>
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
                                    <TableRowColumn>{teacher.age}</TableRowColumn>
                                    <TableRowColumn>+{teacher.phone_number}</TableRowColumn>
                                    <TableRowColumn>{teacher.departament_name}</TableRowColumn>
                                </TableRow>
                            )
                        })}
                    </TableBody>
                </Table>

            </TeachersCardTemplate>
        )
    }
}


export default TeachersView;