import TestCaseCard from "../TestCaseCard/TestCaseCard";

function Test() {
    return <TestCaseCard 
                actual_output = "123"
                expected_output = "456"
                input = "789"
                index = {0}
                code = 'print(456)'
                language = 'python'
            />
}

export default Test;