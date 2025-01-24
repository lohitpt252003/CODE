import TestCaseCard from "../TestCaseCard/TestCaseCard";

function Test() {
    return <TestCaseCard 
                actualOutput = "123"
                expectedOutput = "456"
                input = "789"
                index = {0}
                code = 'print(456)'
                language = 'python'
            />
}

export default Test;