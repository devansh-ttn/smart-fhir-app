const Login = () => {
    const handleLogin = () => {
      window.location.href = `${process.env.REACT_APP_API_BASE}/auth/login`;
    };

    return (
      <div className="login-container">
        <h1>SMART on FHIR Patient Portal</h1>
        <button onClick={handleLogin}>Login with EHR</button>
      </div>
    );
  };