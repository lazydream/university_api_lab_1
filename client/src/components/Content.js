import React from 'react';
import {Switch, Route, Redirect} from 'react-router-dom';

import StudentsSwitch from './students/StudentsSwitch';
import GroupsSwitch from './groups/GroupsSwitch';

const RedirectTo = () => (
    <Redirect to="/students"/>
);

const Content = (props) => (
    <main className="app-content">
        <Switch>
            <Route path="/" exact component={RedirectTo} />
            <Route path="/students" component={StudentsSwitch}/>
            <Route path="/teachers" component={StudentsSwitch}/>
            <Route path="/departaments" component={StudentsSwitch}/>
            <Route path="/courses" component={StudentsSwitch}/>
            <Route path="/groups" component={GroupsSwitch}/>
        </Switch>
    </main>
);

export default Content;