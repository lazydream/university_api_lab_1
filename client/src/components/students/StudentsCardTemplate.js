import React from 'react';
import {Card, CardTitle, CardText} from 'material-ui/Card';
const StudentsCardTemplate = ({children = [], subtitle = ""}) => (
    <Card>
        <CardTitle title="Студенты" subtitle={subtitle}/>
        <CardText>
            {children}
        </CardText>
    </Card>
);

export default StudentsCardTemplate