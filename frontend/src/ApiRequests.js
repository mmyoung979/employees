import React from 'react';

export default class ApiRequests extends React.Component {
    createName() {
        let first_names = ['Kailah', 'Audrie', 'Jaelle', 'Kayceon', 'Khyler', 'Jaheem', 'Kristofer', 'Alyssia', 'Halo', 'Azelia', 'Omari', 'Rayansh', 'Aliyanna', 'Lahna', 'Mathilde', 'Jamira', 'Juliet', 'Misha', 'Yoselyn', 'Nyles'];

        let last_names = ['Hecker', 'Griffith', 'Knutson', 'Pearsall', 'Jolley', 'Byer', 'Towns', 'Staples', 'Gilmartin', 'Prior', 'Barwick', 'Shockley', 'Flory', 'Bushey', 'Nevins', 'Martens', 'Wilton', 'Hailey', 'Halbert', 'Tiffany'];

        let random_index_1 = Math.floor(Math.random() * first_names.length);
        let random_index_2 = Math.floor(Math.random() * last_names.length);

        let data = {
            'first_name': first_names[random_index_1],
            'last_name': last_names[random_index_2],
        }

        let url = `http://localhost:5000?first_name=${data.first_name}&last_name=${data.last_name}`;
        fetch(url, {
            method: 'POST',
        });

        // TODO: Dynamically reload list instead of entire page
        window.location.reload(false);
    }

    deleteAll() {
        let url = 'http://localhost:5000';
        fetch(url, {
            method: 'DELETE',
        });

        // TODO: Dynamically reload list instead of entire page
        setTimeout(() => window.location.reload(false), 1000);
    }

    render() {
        return (
            <div>
                <button onClick={this.createName}>Add Employee</button>
                <button onClick={this.deleteAll}>Delete All Employees</button>
                <hr />
            </div>
        );
    }
}