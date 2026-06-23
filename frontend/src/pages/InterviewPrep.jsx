import { useState } from "react";
import api from "../services/api";

function InterviewPrep() {
  const [resumeText, setResumeText] = useState("");
  const [targetRole, setTargetRole] = useState("");

  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const generateInterview = async () => {
    try {
      setLoading(true);

      const response = await api.post("/interview", {
        resume_text: resumeText,
        target_role: targetRole,
      });

      setResult(response.data);
    } catch (error) {
      console.error(error);
      alert("Interview generation failed");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <h1>Interview Preparation</h1>

      <h3>Resume</h3>

      <textarea
        rows="10"
        cols="100"
        value={resumeText}
        onChange={(e) => setResumeText(e.target.value)}
        placeholder="Paste Resume..."
      />

      <br />
      <br />

      <h3>Target Role</h3>

      <input
        type="text"
        value={targetRole}
        onChange={(e) => setTargetRole(e.target.value)}
        placeholder="AI Engineer"
        style={{
          width: "400px",
          padding: "10px",
        }}
      />

      <br />
      <br />

      <button onClick={generateInterview}>
        Generate Questions
      </button>

      {loading && <p>Generating interview questions...</p>}

      {result && (
        <div style={{ marginTop: "30px" }}>
          <h2>Technical Questions</h2>

          {result.technical_questions?.map((q, index) => (
            <div
              key={index}
              style={{
                border: "1px solid #ddd",
                borderRadius: "8px",
                padding: "15px",
                marginBottom: "15px",
              }}
            >
              <h4>{q.question}</h4>

              <p>
                <strong>Difficulty:</strong> {q.difficulty}
              </p>

              {q.expected_answer && (
                <>
                  <p>
                    <strong>Expected Answer:</strong>
                  </p>
                  <p>{q.expected_answer}</p>
                </>
              )}
            </div>
          ))}

          <h2>Behavioral Questions</h2>

          {result.behavioral_questions?.map((q, index) => (
            <div
              key={index}
              style={{
                border: "1px solid #ddd",
                borderRadius: "8px",
                padding: "15px",
                marginBottom: "15px",
              }}
            >
              <h4>{q.question}</h4>

              <p>
                <strong>Difficulty:</strong> {q.difficulty}
              </p>

              {q.expected_answer && (
                <>
                  <p>
                    <strong>Expected Answer:</strong>
                  </p>
                  <p>{q.expected_answer}</p>
                </>
              )}
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default InterviewPrep;