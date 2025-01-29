import { useEffect, useState } from "react";
import axios from "axios";
import Navbar from '../Navbar/Navbar';

function Users() {
    const [users, setUsers] = useState([]);
    useEffect(() => {
        axios.get("http://localhost:5000/users")  // Adjust URL if needed
            .then(response => {
                console.log(response.data);
                setUsers(response.data);
            })
            .catch(error => {
                console.error("Error fetching users:", error);
            });
    }, []);

    return (
        <div>
            <Navbar />
            <h1>Users</h1>
            <table>
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Username</th>
                        <th>Email</th>
                    </tr>
                </thead>
                <tbody>
                    {users.map((user, i) => (
                        <tr key={user.id}>
                            <td>{user.id}</td>
                            <td><a href={`/users/${user.id}`}>{user.username}</a></td>
                            <td>{user.email}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    )
}


export default Users;