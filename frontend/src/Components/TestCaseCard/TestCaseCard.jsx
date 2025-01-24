import { ToastContainer, toast } from "react-toastify";
import React, { useState } from "react";
import { FaRegClipboard } from "react-icons/fa";
import "react-toastify/dist/ReactToastify.css";
import executeCode from '../../utils/codeExecution';

function TestCaseCard(props) {
  const handleSuccess = (message) => {
    toast.success(message);
  }
  
  const handleError = (message) => {
    toast.error(message);
  }

  const handleInfo = (message) => {
    toast.info(message);
  }

  const handleWarning = (message) => {
    toast.warn(message);
  }
  
  const handleCopyInput = (index) => {
    navigator.clipboard.writeText(props.input)
       .then(() => handleInfo(`Input ${index} copied to clipboard!`))
       .catch((error) => handleWarning(`Error copying input ${index} to clipboard: ` + error.message));
  }

  const handleCopyExpectedOutput = (index) => {
    navigator.clipboard.writeText(props.expected_output)
       .then(() => handleInfo(`Expected Output ${index} copied to clipboard!`))
       .catch((error) => handleWarning(`Error copying expected output ${index} to clipboard: ` + error.message));
  }

  const handleCopyActualOutput = (index) => {
    navigator.clipboard.writeText(props.actual_output)
     .then(() => handleInfo(`Actual Output ${index} copied to clipboard!`))
     .catch((error) => handleWarning(`Error copying actual output ${index} to clipboard: ` + error.message));
  }

  const [actualOutput, setActualOutput] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  const getOutput = async (language, code, input) => {
    try {
      const response = await executeCode(language, code, input); // Assuming executeCode returns a Promise
      if (response.status === 'success') {
        handleSuccess(`Test Case ${props.index + 1} executed successfully!`);
        return response.output;
      }
      else {
        handleWarning(`Test Case ${props.index + 1} execution failed!`);
        return '';
      }
    }
    catch (error) {
      handleError(`Execution error: ${error.message}`);
      return '';
    }
  };

  const handleRunTestCase = async () => {
    setIsLoading(true);
    const code = props.code.trim();
    const language = props.language;
    const input = props.input.trim() || '';
    const expected_output = props.expected_output.trim() || '';

    try {
      const response = await getOutput(language, code, input);
      setActualOutput(response);

      if (response.trim() === expected_output.trim()) {
        handleSuccess(`Test Case ${props.index + 1} passed!`);
      }
      else {
        handleError(
          `Test Case ${props.index + 1} failed! Expected: ${expected_output}, but got: ${response}`
        );
      }
    }
    catch (error) {
      handleError(`Unexpected error while running the test case: ${error.message}`);
    }

    setIsLoading(false);
  };

  return (
      <div>
          <ToastContainer />
          <h3>Test Case {props.index !== undefined ? props.index + 1 : 1}</h3>
          <p>Expected Output: {props.expected_output}</p>
          <p>Input: {props.input}</p>
          <p>Actual Output: {actualOutput}</p>
          <button onClick={handleRunTestCase}>{isLoading ? `Running Testacse ${props.index + 1} .....`  : `Run Testcase ${props.index + 1}`}</button>
          <button onClick={() => props.handleDelete(props.index)}>Delete</button>
          <button onClick={() => handleCopyInput(props.index + 1)}>Copy Input <FaRegClipboard size={18} /></button>
          <button onClick={() => handleCopyExpectedOutput(props.index + 1)}>Copy Expected Output <FaRegClipboard size={18} /></button>
          <button onClick={() => handleCopyActualOutput(props.index + 1)}>Copy Actual Output<FaRegClipboard size={18} /> </button>
      </div>
  )
}

export default TestCaseCard;