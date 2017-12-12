import React, {Component} from 'react';
import TeachersCardTemplate from './TeachersCardTemplate'
import RaisedButton from 'material-ui/RaisedButton';

const Field = ({property, value}) => {
    return (
        <div>
            <p><b>{property}</b></p>
            <span>{value}</span>
        </div>
    )
};

class TeachersDetailedView extends Component {
    constructor(props) {
        super(props);
        this.state = {
            teachers: []
        }
    }
    componentWillMount() {
        const {match: {params}} = this.props;
        const url = `/api/teachers/${params.id}`;
        fetch(url).then(res => res.json())
            .then(teachers => {
                this.setState({
                    teachers
                })
            })
    }

    render() {
        const {teachers} = this.state;
        return (
            <TeachersCardTemplate subtitle="Информация о студенте">
                {teachers.map(teacher => {
                    return (
                        <div>
                            {
                                Object.keys(teacher).map(key => (
                                    <Field
                                        property={key}
                                        value={teacher[key]}
                                        key={key}
                                    />
                                ))
                            }
                            <RaisedButton  primary href={`/api/teachers/${teacher.id}/report`} label="Получить отчет"
                                           style={{marginTop:`10px`}}
                            />
                        </div>
                    )
                })}
            </TeachersCardTemplate>
        )
    }
}


export default TeachersDetailedView;