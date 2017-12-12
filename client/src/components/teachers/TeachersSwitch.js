import React from 'react';
import {Switch, Route} from 'react-router-dom';
import TeachersTable from './TeachersTable';
import TeachersView from './TeachersView';
import FlatButton from 'material-ui/FlatButton';
import  {Toolbar, ToolbarGroup}  from 'material-ui/Toolbar';
import TeachersDetailedView from './TeachersDetailedView'
import TeachersAddView from './TeachersAddView'

const TeachersSwitch = (props) => (
    <section>
        <Toolbar>
            <ToolbarGroup>
                <FlatButton href="/teachers/table" label="Таблица" />
                <FlatButton href="/teachers/view" label="Представление" />
                <FlatButton href="/teachers/add" label="Добавить преподавателя" />
            </ToolbarGroup>
        </Toolbar>
        <Switch>
            <Route path="/teachers/table" exact component={TeachersTable}/>
            <Route path="/teachers" exact component={TeachersTable}/>
            <Route path="/teachers/view" exact component={TeachersView}/>
            <Route path="/teachers/details/:id" exact component={TeachersDetailedView}/>
            <Route path="/teachers/add" exact component={TeachersAddView}/>
        </Switch>
    </section>
);

export default TeachersSwitch;