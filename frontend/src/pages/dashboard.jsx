import { Link } from "react-router-dom";

function Dashboard() {
  const cardStyle = {
    background: "white",
    padding: "25px",
    borderRadius: "12px",
    boxShadow: "0 2px 10px rgba(0,0,0,0.1)",
    textDecoration: "none",
    color: "#111827"
  };

  return (
    <div>
      <div
        style={{
          background: "#111827",
          color: "white",
          padding: "30px",
          borderRadius: "12px",
          marginBottom: "30px"
        }}
      >
        <h1>AI Career Copilot</h1>
        <p>
          Resume Analysis, JD Matching, Interview Preparation and AI Career Guidance
        </p>
      </div>

      <div
        style={{
          display: "grid",
          gridTemplateColumns: "repeat(auto-fit, minmax(250px, 1fr))",
          gap: "20px"
        }}
      >
        <Link to="/resume" style={cardStyle}>
          <h2>📄 Resume Analyzer</h2>
          <p>Analyze strengths and missing skills.</p>
        </Link>

        <Link to="/jd" style={cardStyle}>
          <h2>🎯 JD Matcher</h2>
          <p>Match your resume against jobs.</p>
        </Link>

        <Link to="/interview" style={cardStyle}>
          <h2>💼 Interview Prep</h2>
          <p>Generate interview questions.</p>
        </Link>

        <Link to="/career" style={cardStyle}>
          <h2>🚀 Career Advisor</h2>
          <p>Get career guidance using RAG.</p>
        </Link>

        <Link to="/copilot" style={cardStyle}>
          <h2>🤖 AI Copilot</h2>
          <p>Chat with your AI career assistant.</p>
        </Link>
      </div>
    </div>
  );
}

export default Dashboard;