import React, {Component} from 'react';
import {
    Table,
    TableBody,
    TableHeader,
    TableHeaderColumn,
    TableRow,
    TableRowColumn,
} from 'material-ui/Table';
import GroupsCardTemplate from './GroupsCardTemplate'

class GroupsTable extends Component {
    constructor(props) {
        super(props);
        this.state = {
            groups: []
        }
    }
    componentWillMount() {
        const url = `/api/groups`;
        fetch(url).then(res => res.json())
            .then(groups => {
                this.setState({
                    groups
                })
            })
    }

    render() {
        const {groups} = this.state;
        return (
            <GroupsCardTemplate subtitle="Таблица">
                <Table
                    selectable={false}
                >
                    <TableHeader
                        adjustForCheckbox={false}
                        displaySelectAll={false}
                    >
                        <TableRow>
                            <TableHeaderColumn>Код</TableHeaderColumn>
                            <TableHeaderColumn>Название</TableHeaderColumn>
                            <TableHeaderColumn>Код кафедры</TableHeaderColumn>
                        </TableRow>
                    </TableHeader>
                    <TableBody
                        displayRowCheckbox={false}
                    >
                        {groups.map(group => {
                            return (
                                <TableRow>
                                    <TableRowColumn>{group.id}</TableRowColumn>
                                    <TableRowColumn>{group.name}</TableRowColumn>
                                    <TableRowColumn>{group.departament_id}</TableRowColumn>
                                </TableRow>
                            )
                        })}
                    </TableBody>
                </Table>
            </GroupsCardTemplate>
        )
    }
}


export default GroupsTable;