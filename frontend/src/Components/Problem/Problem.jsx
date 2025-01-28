import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useParams } from 'react-router-dom';
import TestCases from '../TestCases/TestCases';
import Navbar from '../Navbar/Navbar';

function Problem() {
  const { id } = useParams();
  // console.log(id);
  // props.id = id;
  
  // console.log(props.id);
  
  const [title, setTitle] = useState('');
  const [problemStatement, setProblemStatement] = useState('');
  const [testcases, setTestcases] = useState({});
  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get(`/problems/${id}`);
        // console.log(response.data.testcases);
        setProblemStatement(response.data.statement);
        setTestcases(response.data.testcases);
        setTitle(response.data.name);
        
      }
      catch (error) {
        console.error("Error fetching data:", error);
      }
    };

    fetchData();
  }, []);

  return (
    <div>
      <Navbar />
      <h1>{title}</h1>
      <p>{problemStatement}</p>
      <TestCases 
        id = {id}
        testcases = {testcases}
        type = {"visible"}
      />
    </div>
  );
}

export default Problem;