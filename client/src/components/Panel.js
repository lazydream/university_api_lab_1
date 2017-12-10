import React from 'react';
import {Card, CardText} from 'material-ui/Card';
import {Route, Link} from 'react-router-dom';

const Panel =  (props) => (
  <Card className="app-aside-panel">
      <CardText>
          Hey, ama panel
      </CardText>
  </Card>
);

export default Panel;