import React, { useEffect, useState } from 'react';
import axios from 'axios';

function LandingPage() {
    const [names, setNames] = useState([]);

    useEffect(() => {
        let apiCall = async () => {
            const response = await axios.get('http://127.0.0.1:5000/');
            console.log(response.data.names);
            setNames(response.data.names);
        }
        apiCall();
    }, []); // Empty dependency array to call the API only once when the component mounts

    return (
        <div>
            {
                names.map((name, index) => {
                    return <h1 key={index}>{name}</h1>; // Added return and key
                })
            }
        </div>
    );
}

export default LandingPage;
