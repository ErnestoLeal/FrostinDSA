import React from 'react';
import './App.css';
import CodeRunner from './components/CodeRunner';  // Import the CodeRunner component

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Welcome to the Code Executor</h1>
      </header>
      <CodeRunner />  {/* Use the CodeRunner component here */}
    </div>
  );
}

export default App;
