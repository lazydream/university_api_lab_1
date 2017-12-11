import React from 'react';
import {Switch, Route} from 'react-router-dom';
import GroupsTable from './GroupsTable';
import FlatButton from 'material-ui/FlatButton';
import  {Toolbar, ToolbarGroup}  from 'material-ui/Toolbar';
import GroupsAddView from './GroupsAddView'

const GroupsSwitch = (props) => (
    <section>
        <Toolbar>
            <ToolbarGroup>
                <FlatButton href="/groups/table" label="Таблица" />
                <FlatButton href="/groups/add" label="Добавить группу" />
            </ToolbarGroup>
        </Toolbar>
        <Switch>
            <Route path="/groups/table" exact component={GroupsTable}/>
            <Route path="/groups" exact component={GroupsTable}/>
            <Route path="/groups/add" exact component={GroupsAddView}/>
        </Switch>
    </section>
);

export default GroupsSwitch;