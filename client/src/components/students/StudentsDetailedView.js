import React, {Component} from 'react';
import StudentsCardTemplate from './StudentsCardTemplate'


const Field = ({property, value}) => {
    return (
        <div>
            <p><b>{property}</b></p>
            <span>{value}</span>
        </div>
    )
};

class StudentsDetailedView extends Component {
    constructor(props) {
        super(props);
        this.state = {
            students: []
        }
    }
    componentWillMount() {
        const {match: {params}} = this.props;
        const url = `/api/students/${params.id}`;
        fetch(url).then(res => res.json())
            .then(students => {
                this.setState({
                    students
                })
            })
    }

    render() {
        const {students} = this.state;
        console.log(students);
        return (
            <StudentsCardTemplate subtitle="Информация о студенте">
                {students.map(student => {
                    return (
                        <div>
                            {
                                Object.keys(student).map(key => (
                                    <Field
                                        property={key}
                                        value={student[key]}
                                        key={key}
                                    />
                                ))
                            }
                        </div>
                    )
                })}
            </StudentsCardTemplate>
        )
    }
}


export default StudentsDetailedView;