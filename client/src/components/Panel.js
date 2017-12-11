import React from 'react';
import {Card, CardText} from 'material-ui/Card';
import {List, ListItem} from 'material-ui/List';
import {NavLink} from 'react-router-dom';

const Panel =  (props) => (
  <Card className="app-aside-panel">
      <CardText>
          <List>
              <ListItem>
                  <NavLink to="/students">Студенты</NavLink>
              </ListItem>
              <ListItem>
                  <NavLink to="/teachers">Преподаватели</NavLink>
              </ListItem>
              <ListItem>
                  <NavLink to="/courses">Курсы</NavLink>
              </ListItem>
              <ListItem>
                  <NavLink to="/departaments">Кафедры</NavLink>
              </ListItem>
              <ListItem>
                  <NavLink to="/groups">Группы</NavLink>
              </ListItem>
          </List>
      </CardText>
  </Card>
);

export default Panel;