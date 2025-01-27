import React, { useEffect, useState } from 'react';
import axios from 'axios';
import TestCaseCard from '../TestCaseCard/TestCaseCard';
import executeCode from '../../utils/codeExecution';

function TestCases(props) {
    const [cases, setCases] = useState([]);
    useEffect(() => {
        const fetchData = async () => {
          try {
            const response = await axios.get(`/testcases/${props.id}`);
            // console.log(response.data.cases);
            setCases(response.data.cases);
          }
          catch (error) {
            console.error("Error fetching data:", error);
          }
        };
    
        fetchData();
    }, []);
    // console.log(props.language);
      
    // console.log(actualOutputs);
    const [runTestCases_message, setRunTestCases_message] = useState(`Run All Testcases`);
    const runTestCase = async (i) => {
      const response = await executeCode(props.language, props.code, cases[i].input);
      // console.log(response);
      setRunTestCases_message(`Runninng Testcase ${i + 1}`);
      let element = document.getElementById(`case-${i}`);
      element.innerText = `Actual Output: ${response.output}`;
    }
    

    const runAllTestCases = async () => {
      setRunTestCases_message('Running All Testcases...');
      for (let i = 0; i < cases.length; i++) {
        await runTestCase(i);
      }
      setRunTestCases_message('Run All Testcases');
    }

    // console.log(actualOutputs);
    
    
    

    return (
        <div>
            <h2>Test Cases</h2>
            <button onClick={runAllTestCases}>{runTestCases_message}</button>
            
            {
                cases.map((_case, i) => 
                <TestCaseCard 
                    index = {i}
                    expectedOutput = {_case.expected_output}
                    input = {_case.input}
                    code = {props.code}
                    language = {props.language}
                    key = {i}
                    id = {`case-${i}`}
                />)
            }
        </div>
    );
}

export default TestCases;