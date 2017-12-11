import React, {Component} from 'react';
import {Redirect} from 'react-router-dom';
import StudentsCardTemplate from './StudentsCardTemplate'
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
    addStudent = () => {
        const url = `/api/students`;
        const data = {};
        const inputs = this.refs.form.querySelectorAll('input[name]');
        inputs.forEach(input => {
            data[input.name] = input.value;
            if (input.name === 'group_id') {
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
        if (this.state.done) return <Redirect to="/students/view" />
        return (
            <StudentsCardTemplate subtitle="Добавить">
                <form ref="form">
                    <Input property="name" label="ФИО"/>
                    <Input property="birth_data" label="Дата рождения"/>
                    <Input property="gender" label="Пол"/>
                    <Input property="phone_number" label="Номер телефона"/>
                    <Input property="group_id" label="Код группы"/>
                    <RaisedButton  primary onClick={this.addStudent} label="Добавить"
                                   style={{marginTop:`10px`}}
                    />
                </form>
            </StudentsCardTemplate>
        )
    }
}


export default StudentsDetailedView;