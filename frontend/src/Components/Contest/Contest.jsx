import { useParams } from 'react-router-dom';
import React, { useEffect, useState } from 'react';
import axios from 'axios';
import Navbar from '../Navbar/Navbar'

function Contest() {
    const { id } = useParams();
    const [problems, setProblems] = useState([]);
    useEffect(() => {
        // Fetching the list of problems from the API
        axios.get(`/contests/${id}`)
          .then(response => {
            // console.log(response.data);
            setProblems(response.data);
          })
          .catch(error => {
            console.error('Error fetching problems:', error);
          });
    }, []);
    // console.log(problems);
    
    return(
        <div>
            <Navbar />
            <h1>Contest: {id}</h1>
            <ul>
                {
                    problems.map((problem, i) =>
                        <li key={i}><a href={`/problems/${problem}`}>{problem}</a></li>
                    )
                }
            </ul>
        </div>
    );
}


export default Contest;