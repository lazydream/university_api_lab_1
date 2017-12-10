import React from 'react';
import {Switch, Route} from 'react-router-dom';

import StudentsSwitch from './students/StudentsSwitch';

const HelloWorld = () => (
    <div >
        Hello!
    </div>
);

const Content = (props) => (
    <main className="app-content">
        <Switch>
            <Route path="/" exact component={HelloWorld} />
            <Route path="/students" component={StudentsSwitch}/>
        </Switch>
    </main>
);

export default Content;