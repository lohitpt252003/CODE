import React, { useEffect, useState } from 'react';
import axios from 'axios';

const Problems = () => {
  const [problems, setProblems] = useState([]);

  useEffect(() => {
    // Fetching the list of problems from the API
    axios.get('/problems')
      .then(response => {
        // console.log(response.data);
        setProblems(response.data);
      })
      .catch(error => {
        console.error('Error fetching problems:', error);
      });
  }, []);

  return (
    <div className="Problems-container">
      <h1 className="Problems-Title">Available Problems</h1>
      <ul className="Problems-problems">
        {
            problems.map((problem, i) => 
                <li key={i}><a href={`/problems/${i + 1}`}>{problem}</a></li>
            )
        }
      </ul>
    </div>
  );
};

export default Problems;
