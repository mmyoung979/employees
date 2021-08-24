import React from 'react';

export default class FetchApi extends React.Component {
    state = {
        loading: true,
        refresh: false,
        employees: null,
    };

    async componentDidMount() {
        const url = "http://localhost:5000/";
        const response = await fetch(url);
        const data = await response.json();
        this.setState({
            loading: false,
            employees: data.employees
        });
    }

    render() {
        return (
            <div>
                {this.state.loading ? <div>Loading API data...</div> : this.state.employees.map((employee, index) => {
                    return <div key={index}>{employee.first_name} {employee.last_name}</div>
                })}
            </div>
        )
    }
}