import React from 'react';
import {Card, CardTitle, CardText} from 'material-ui/Card';
const TeachersCardTemplate = ({children = [], subtitle = ""}) => (
    <Card>
        <CardTitle title="Преподаватели" subtitle={subtitle}/>
        <CardText>
            {children}
        </CardText>
    </Card>
);

export default TeachersCardTemplate