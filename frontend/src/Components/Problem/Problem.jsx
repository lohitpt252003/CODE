import React, { useEffect, useState } from 'react';
import axios from 'axios';
import TestCases from '../TestCases/TestCases';

function Problem(props) {
  const [problemStatement, setProblemStatement] = useState('');
  const [testcases, setTestcases] = useState({});
  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get(`/problems/${props.id}`);
        // console.log(response.data.testcases);
        setProblemStatement(response.data.statement);
        setTestcases(response.data.testcases);
      }
      catch (error) {
        console.error("Error fetching data:", error);
      }
    };

    fetchData();
  }, []);

  return (
    <div>
      <p>{problemStatement}</p>
      <form action="" method="get"></form>
      <TestCases 
        id = {props.id}
        testcases = {testcases}
        type = {"visible"}
      />
    </div>
  );
}

export default Problem;