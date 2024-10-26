import React, { useState } from 'react';
import axios from 'axios';

function CodeRunner() {
  const [code, setCode] = useState('');
  const [output, setOutput] = useState('');
  const [error, setError] = useState('');

  const runCode = async () => {
    try {
      // Make sure this matches your Django endpoint
      const response = await axios.post('http://localhost:8000/code_executor/execute/', { code });
      setOutput(response.data.output);
      setError(response.data.error);
    } catch (err) {
      setError('An error occurred while running the code.');
    }
  };

  return (
    <div>
      <h2>Run Python Code</h2>
      <textarea 
        rows="10" 
        cols="30" 
        value={code} 
        onChange={(e) => setCode(e.target.value)} 
        placeholder="Enter your Python code here..."
      />
      <br />
      <button onClick={runCode}>Run Code</button>
      <h3>Output:</h3>
      <pre>{output}</pre>
      {error && <pre style={{ color: 'red' }}>Error: {error}</pre>}
    </div>
  );
}

export default CodeRunner;
