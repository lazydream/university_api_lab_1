import React, {Component} from 'react';
import {Redirect} from 'react-router-dom';
import TeachersCardTemplate from './TeachersCardTemplate'
import RaisedButton from 'material-ui/RaisedButton';

const Input = ({property, label}) => {
    return (
        <div>
            <p><b>{label}</b></p>
            <input name={property} type="text"/>
        </div>
    )
};

class TeachersDetailedView extends Component {
    constructor(props) {
        super(props);
        this.state = {
            done: false
        }
    }
    addTeacher = () => {
        const url = `/api/teachers`;
        const data = {};
        const inputs = this.refs.form.querySelectorAll('input[name]');
        inputs.forEach(input => {
            data[input.name] = input.value;
            if (input.name === 'course_id' || input.name === 'departament_id') {
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
        if (this.state.done) return <Redirect to="/teachers/view" />
        return (
            <TeachersCardTemplate subtitle="Добавить">
                <form ref="form">
                    <Input property="name" label="ФИО"/>
                    <Input property="birth_date" label="Дата рождения"/>
                    <Input property="gender" label="Пол"/>
                    <Input property="departament_id" label="Код кафедры"/>
                    <Input property="phone_number" label="Номер телефона"/>
                    <RaisedButton  primary onClick={this.addTeacher} label="Добавить"
                                   style={{marginTop:`10px`}}
                    />
                </form>
            </TeachersCardTemplate>
        )
    }
}


export default TeachersDetailedView;