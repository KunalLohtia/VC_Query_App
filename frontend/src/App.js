import React from 'react';

function App() {
    const handleLogin = () => {
        window.location.href = 'http://localhost:5000/login';  // Flask OAuth endpoint
    };

    return (
        <div>
            <button onClick={handleLogin}>Login with Google</button>
        </div>
    );
}

export default App;