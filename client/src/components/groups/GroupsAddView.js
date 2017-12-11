import React, {Component} from 'react';
import {Redirect} from 'react-router-dom';
import GroupsCardTemplate from './GroupsCardTemplate'
import RaisedButton from 'material-ui/RaisedButton';

const Input = ({property, label}) => {
    return (
        <div>
            <p><b>{label}</b></p>
            <input name={property} type="text"/>
        </div>
    )
};

class StudentsDetailedView extends Component {
    constructor(props) {
        super(props);
        this.state = {
            done: false
        }
    }
    addGroup = () => {
        const url = `/api/groups`;
        const data = {};
        const inputs = this.refs.form.querySelectorAll('input[name]');
        inputs.forEach(input => {
            data[input.name] = input.value;
            if (input.name === 'departament_id') {
                data[input.name] = +input.value;
            }
        });
        fetch(url,  {
            method: 'POST',
            body: JSON.stringify([data])
        }).then(() => {
            this.setState({done:true})
        })
    };

    render() {
        if (this.state.done) return <Redirect to="/groups/table" />
        return (
            <GroupsCardTemplate subtitle="Добавить">
                <form ref="form">
                    <Input property="name" label="Название"/>
                    <Input property="departament_id" label="Код кафедры"/>
                    <RaisedButton  primary onClick={this.addGroup} label="Добавить"
                                   style={{marginTop:`10px`}}
                    />
                </form>
            </GroupsCardTemplate>
        )
    }
}


export default StudentsDetailedView;