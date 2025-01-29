import React, { useEffect, useState } from 'react';
import axios from 'axios';
import Navbar from '../Navbar/Navbar';



function Contests() {
    const [contests, setContests] = useState([])
    useEffect(() => {
        // Fetching the list of problems from the API
        axios.get('/contests')
          .then(response => {
            console.log(response.data);
            setContests(response.data);
          })
          .catch(error => {
            console.error('Error fetching problems:', error);
          });
      }, []);
    return(
        <div>
          <Navbar />
            <h1>Contests</h1>
            <ul>
              {
                  contests.map((contest, i) => 
                      <li key={i}><a href={`/contests/${i + 1}`}>contest {i + 1}</a></li>
                  )
              }
            </ul>
        </div>
    )
}


export default Contests