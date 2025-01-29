import { useParams } from 'react-router-dom';
import React, { useEffect, useState } from 'react';
import axios from 'axios';
import Navbar from '../Navbar/Navbar'



function User() {
    const { id } = useParams();
    const [user, setUser] = useState([]);
    const [problems, setProblems] = useState([]);
    const [contests, setContests] = useState([]);
    useEffect(() => {
        // Fetching the list of problems from the API
        axios.get(`/users/${id}`)
          .then(response => {
            //   console.log(response.data);
              setUser(response.data);
            //   console.log(response.data.solved_problems);
              setProblems(response.data.solved_problems);
            //   console.log(response.data.contests_joined);
              setContests(response.data.contests_joined);
              
          })
          .catch(error => {
            console.error('Error fetching problems:', error);
          });
    }, []);
    return (
        <div>
            <Navbar />
            <h1>User Details</h1>
            <p>ID: {user.id}</p>
            <p>Username: {user.username}</p>
            <p>Email: {user.email}</p>
            <div>
                <h1>Problems Solved</h1>
                <ul>
                <h1>{problems.length === 0 ? "No problems solved" : ""}</h1>
                    {
                        problems.map((problem, i) =>
                            <li key={i}><a href={`/problems/${problem}`}>{problem}</a></li>
                        )
                    }
                </ul>
            </div>
            <div>
                <h1>Contests Attended</h1>
                <ul>
                    <h1>{contests.length === 0 ? "No contests attended" : ""}</h1>
                    {
                        contests.map((contest, i) =>
                            <li key={i}><a href={`/contests/${contest}`}>{contest}</a></li>
                        )
                    }
                </ul>
            </div>
        </div>
    )
}

export default User;