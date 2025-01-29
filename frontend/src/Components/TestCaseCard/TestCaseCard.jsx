import { NotificationContainer, NotificationManager } from 'react-notifications';
import 'react-notifications/lib/notifications.css';

import React, { useState } from "react";
import { FaRegClipboard } from "react-icons/fa";
import PropTypes from "prop-types";

import executeCode from '../../utils/codeExecution';

function TestCaseCard(props) {
  const handleSuccess = (message) => {
    // NotificationManager.success('Success message', 'Title here');
  }
  
  const handleError = (message) => {
    // NotificationManager.error('Error message', 'Click me!', 5000, () => {
      // alert('callback');
    // });
  }
  
  const handleInfo = (message) => {
    // NotificationManager.info('Info message');
  }
  
  const handleWarning = (message) => {
    // NotificationManager.warning('Warning message', 'Close after 3000ms', 3000);
  }
  
  const handleCopyInput = (index) => {
    navigator.clipboard.writeText(props.input)
       .then(() => handleInfo(`Input ${index} copied to clipboard!`))
       .catch((error) => handleWarning(`Error copying input ${index} to clipboard: ` + error.message));
  }

  const handleCopyExpectedOutput = (index) => {
    navigator.clipboard.writeText(props.expectedOutput)
       .then(() => handleInfo(`Expected Output ${index} copied to clipboard!`))
       .catch((error) => handleWarning(`Error copying expected output ${index} to clipboard: ` + error.message));
  }

  const handleCopyActualOutput = (index) => {
    
    navigator.clipboard.writeText(actualOutput)
     .then(() => handleInfo(`Actual Output ${index} copied to clipboard!`))
     .catch((error) => handleWarning(`Error copying actual output ${index} to clipboard: ` + error.message));
  }

  const [actualOutput, setActualOutput] = useState(`Actual Output: `);
  const [isLoading, setIsLoading] = useState(false);

  const handleRunTestCase = async () => {
    setIsLoading(true);
    const code = props.code.trim();
    // console.log(code);
    
    const language = props.language;
    const input = props.input.trim();
    const expectedOutput = props.expectedOutput.trim();
    const response = await executeCode(language, code, input);
    if (response.status === 'success') {
      handleSuccess(`Code executed successfully!`)
      setActualOutput(`Actual Output: ` + response.output);
    }
    // console.log(response);
        
    setIsLoading(false);
  }

  return (
      <div>
          {/* <button onClick={showNotification}>Click</button> */}
          {/* <NotificationContainer /> */}
          <h3>Test Case {props.index !== undefined ? props.index + 1 : 1}</h3>
          <p>Expected Output: <pre>{props.expectedOutput}</pre></p>
          <p>Input: <pre>{props.input}</pre></p>
          <p  id={`case-${props.index}`}><pre>{actualOutput}</pre></p>
          <button onClick={handleRunTestCase}>{isLoading ? `Running Testacse ${props.index + 1} .....`  : `Run Testcase ${props.index + 1}`}</button>
          <button onClick={() => props.handleDelete(props.index)}>Delete</button>
          <button onClick={() => handleCopyInput(props.index + 1)}>Copy Input <FaRegClipboard size={18} /></button>
          <button onClick={() => handleCopyExpectedOutput(props.index + 1)}>Copy Expected Output <FaRegClipboard size={18} /></button>
          <button onClick={() => handleCopyActualOutput(props.index + 1)}>Copy Actual Output<FaRegClipboard size={18} /> </button>
      </div>
  )
}

TestCaseCard.defaultProps  = {
  input: '',
  expectedOutput: '',
  code: '// Write your code here',
  language: 'javascript',
  index: 0,
}

TestCaseCard.propTypes = {
  index: PropTypes.number,
  input: PropTypes.string,
  expectedOutput: PropTypes.string,
  code: PropTypes.string,
  language: PropTypes.string,
}

export default TestCaseCard;