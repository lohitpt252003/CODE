import React, { useEffect, useState } from 'react';
import { Editor } from "@monaco-editor/react";
import TestCaseCard from '../TestCaseCard/TestCaseCard';
import executeCode from '../../utils/codeExecution';

function TestCases(props) {
    const [language, setLanguage] = useState("cpp");
    const languageMap = {
      cpp: `#include <iostream>\nusing namespace std;\n\nint main() {\n\tcout << "Hello, C++!" << endl;\n\treturn 0;\n}`,
      c: `#include <stdio.h>\n\nint main() {\n\tprintf("Hello, C!\\n");\n\treturn 0;\n}`,
      python: `print("Hello, Python!")`,
      java: `public class Main {\n\tpublic static void main(String[] args) {\n\t\tSystem.out.println("Hello, Java!");\n\t}\n}`,
      javascript: `console.log("Hello, JavaScript!");`,
    };
    const languages = ["cpp", "c", "python", "java", "javascript"];
    const [boilerplate, setBoilerplate] = useState(languageMap[language]);

    const handleLanguageChange = (lang) => {
      setLanguage(lang);
      setBoilerplate(languageMap[lang]); // Update boilerplate for selected language
    };
    const handleEditorChange = (newValue) => {
      setBoilerplate(newValue);
      // console.log(newValue);
    };

    const [_testcases, set_testcases] = useState([]);
    useEffect(() => {
      // Set _testcases when props.testcases.visible changes
      set_testcases(props.testcases.visible);
    }, [props.testcases.visible]);
    console.log(_testcases);
    
    
    const [runTestCases_message, setRunTestCases_message] = useState(`Run All Testcases`);
    const runTestCase = async (i) => {
      const response = await executeCode(language, boilerplate, _testcases[i].input);
      // console.log(response);
      setRunTestCases_message(`Runninng Testcase ${i + 1}`);
      let element = document.getElementById(`case-${i}`);
      element.innerText = `Actual Output: ${response.output}`;
    }
    

    const runAllTestCases = async () => {
      setRunTestCases_message('Running All Testcases...');
      for (let i = 0; i < _testcases.length; i++) {
        await runTestCase(i);
      }
      setRunTestCases_message('Run All Testcases');
    }
    
    return (
        <div>
            {/* <h2>{props.testCaseType}</h2>
            <button onClick={runAllTestCases}>{runTestCases_message}</button>
            <select
              value={language}
              onChange={(event) => handleLanguageChange(event.target.value)}
            >
              {languages.map((lang) => (
                <option key={lang} value={lang}>
                  {lang}
                </option>
              ))}
            </select> */}

            {/* <Editor
              height="50vh"
              language={language} // Correct language binding
              value={boilerplate} // Dynamically set the editor content
              theme="vs-dark"
              options={{
                scrollBeyondLastLine: false,
                smoothScrolling: true,
              }}
              // onChange={(newValue) => setBoilerplate(newValue)} // Update boilerplate as user edits
              onChange={handleEditorChange}
            /> */}

            {/* {
                _testcases.map((_case, i) => 
                <TestCaseCard 
                    index = {i}
                    expectedOutput = {_case.expected_output}
                    input = {_case.input}
                    code = {boilerplate}
                    language = {language}
                    key = {i}
                    id = {`case-${i}`}
                />)
            } */}
        </div>
    );
}

export default TestCases;