import React from 'react';
import {Card, CardTitle, CardText} from 'material-ui/Card';

const GroupsCardTemplate = ({children = [], subtitle = ""}) => (
    <Card>
        <CardTitle title="Группы" subtitle={subtitle}/>
        <CardText>
            {children}
        </CardText>
    </Card>
);

export default GroupsCardTemplate