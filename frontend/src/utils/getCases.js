import axios from 'axios';

async function getCases(id) {
    try {
        const response = await axios.get(`http://127.0.0.1:5000/testcases/${id}`);
        console.log(response.data.cases); // Debugging purposes
        return response.data.cases; // Return the fetched cases
    } catch (error) {
        console.error("Error fetching cases:", error);
        return []; // Return an empty array in case of an error
    }
}

export default getCases;
