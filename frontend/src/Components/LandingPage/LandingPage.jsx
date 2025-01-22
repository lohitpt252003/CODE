import React, { useEffect, useState } from 'react';
import axios from 'axios';
import getCases from '../../utils/getCases';

function LandingPage() {
    let callGetCases = async () => {
        let res = await getCases(1);
        console.log(res);
    }
    
    const [actualCases, setActualCases] = useState([]);

    useEffect(() => {
        let apiCall = async () => {
            const response = await axios.get('http://127.0.0.1:5000/testcases/1');
            console.log(response.data.cases);
            setActualCases(response.data.cases);
        }
        apiCall();
    }, []);

    return (
        <div>
            <h1>Number of cases: {actualCases.length}</h1>
            {
                actualCases.map((caseItem, index) => (
                    <h1 key={index}>
                        Expected Output: {caseItem.expected_output} <br />
                        Input: {caseItem.input}
                    </h1>
                ))
            }

        </div>
    );
}

export default LandingPage;
