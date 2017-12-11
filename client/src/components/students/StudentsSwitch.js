import React from 'react';
import {Switch, Route, Link} from 'react-router-dom';
import StudentsTable from './StudentsTable';
import StudentsView from './StudentsView';
import FlatButton from 'material-ui/FlatButton';
import  {Toolbar, ToolbarGroup}  from 'material-ui/Toolbar';
import StudentsDetailedView from './StudentsDetailedView'
import StudentsAddView from './StudentsAddView'

const StudentsSwitch = (props) => (
    <section>
        <Toolbar>
            <ToolbarGroup>
                <FlatButton href="/students/table" label="Таблица" />
                <FlatButton href="/students/view" label="Представление" />
                <FlatButton href="/students/add" label="Добавить студента" />
            </ToolbarGroup>
        </Toolbar>
        <Switch>
            <Route path="/students/table" exact component={StudentsTable}/>
            <Route path="/students" exact component={StudentsTable}/>
            <Route path="/students/view" exact component={StudentsView}/>
            <Route path="/students/details/:id" exact component={StudentsDetailedView}/>
            <Route path="/students/add" exact component={StudentsAddView}/>
        </Switch>
    </section>
);

export default StudentsSwitch;