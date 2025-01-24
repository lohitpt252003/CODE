import { useEffect, useState } from "react";
import getCases from "../../utils/getCases";

function Problem() {
  const [cases, setCases] = useState([]);

  useEffect(() => {
    async function fetchCases() {
      const data = await getCases(1); // Fetch cases with id = 1
      // console.log(data.cases);      
      setCases(data.cases); // Update the state with the fetched cases
    }
    
    fetchCases(); // Call the fetchCases function
  }, []); // Empty dependency array ensures this runs once when the component mounts

  return (
    <div>
      <h1>Problem Test Cases</h1>
      {cases.length > 0 ? (
        <ul>
          {cases.map((testCase, index) => (
            <li key={index}>{JSON.stringify(testCase)}</li>
          ))}
        </ul>
      ) : (
        <p>No cases found.</p>
      )}
    </div>
  );
}

export default Problem;
