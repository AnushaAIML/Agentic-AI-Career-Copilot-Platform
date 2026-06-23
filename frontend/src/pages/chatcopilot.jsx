import { useState } from "react";
import api from "../services/api";

function ChatCopilot() {
  const [userInput, setUserInput] = useState("");
  const [resumeText, setResumeText] = useState("");
  const [jobDescription, setJobDescription] = useState("");
  const [targetRole, setTargetRole] = useState("");

  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const askCopilot = async () => {
    try {
      setLoading(true);

      const response = await api.post("/chat", {
        user_input: userInput,
        resume_text: resumeText,
        job_description: jobDescription,
        target_role: targetRole,
      });

      setResult(response.data);
    } catch (error) {
      console.error(error);

      alert(
        JSON.stringify(
          error.response?.data || error.message,
          null,
          2
        )
      );
    } finally {
      setLoading(false);
    }
  };

  const cardStyle = {
    background: "white",
    padding: "20px",
    borderRadius: "12px",
    boxShadow: "0 2px 10px rgba(0,0,0,0.1)",
    marginTop: "20px",
  };

  return (
    <div>
      <h1>🤖 AI Career Copilot</h1>

      <input
        type="text"
        value={userInput}
        onChange={(e) => setUserInput(e.target.value)}
        placeholder="Ask anything..."
        style={{
          width: "100%",
          padding: "12px",
          marginBottom: "15px",
        }}
      />

      <textarea
        rows="5"
        value={resumeText}
        onChange={(e) => setResumeText(e.target.value)}
        placeholder="Resume (Optional)"
        style={{
          width: "100%",
          padding: "12px",
          marginBottom: "15px",
        }}
      />

      <textarea
        rows="5"
        value={jobDescription}
        onChange={(e) => setJobDescription(e.target.value)}
        placeholder="Job Description (Optional)"
        style={{
          width: "100%",
          padding: "12px",
          marginBottom: "15px",
        }}
      />

      <input
        type="text"
        value={targetRole}
        onChange={(e) => setTargetRole(e.target.value)}
        placeholder="Target Role (Optional)"
        style={{
          width: "100%",
          padding: "12px",
          marginBottom: "20px",
        }}
      />

      <button onClick={askCopilot}>Send</button>

      {loading && (
        <p style={{ marginTop: "20px" }}>
          Thinking...
        </p>
      )}

      {result && (
        <div style={cardStyle}>
          <h3>Selected Tool: {result.selected_tool}</h3>

          {result.result?.answer && (
            <>
              <h2>Answer</h2>

              <p
                style={{
                  whiteSpace: "pre-wrap",
                  lineHeight: "1.8",
                }}
              >
                {result.result.answer}
              </p>

              {result.result.sources && (
                <>
                  <h3>Sources</h3>

                  {result.result.sources.map((source, index) => (
                    <span
                      key={index}
                      style={{
                        display: "inline-block",
                        background: "#dbeafe",
                        color: "#1d4ed8",
                        padding: "8px 12px",
                        borderRadius: "20px",
                        marginRight: "10px",
                        marginBottom: "10px",
                      }}
                    >
                      {source}
                    </span>
                  ))}
                </>
              )}
            </>
          )}

          {result.result?.summary && (
            <>
              <h2>Summary</h2>
              <p>{result.result.summary}</p>

              <h2>Skills</h2>
              <ul>
                {result.result.skills?.map((skill, i) => (
                  <li key={i}>{skill}</li>
                ))}
              </ul>

              <h2>Strengths</h2>
              <ul>
                {result.result.strengths?.map((item, i) => (
                  <li key={i}>{item}</li>
                ))}
              </ul>

              <h2>Missing Skills</h2>
              <ul>
                {result.result.missing_skills?.map((item, i) => (
                  <li key={i}>{item}</li>
                ))}
              </ul>
            </>
          )}

          {result.result?.match_score !== undefined && (
            <>
              <h2>
                Match Score: {result.result.match_score}%
              </h2>

              <h3>Matching Skills</h3>

              <ul>
                {result.result.matching_skills?.map((skill, i) => (
                  <li key={i}>{skill}</li>
                ))}
              </ul>

              <h3>Missing Skills</h3>

              <ul>
                {result.result.missing_skills?.map((skill, i) => (
                  <li key={i}>{skill}</li>
                ))}
              </ul>

              <h3>Recommendations</h3>

              <ul>
                {result.result.recommendations?.map((item, i) => (
                  <li key={i}>{item}</li>
                ))}
              </ul>
            </>
          )}

          {result.result?.technical_questions && (
            <>
              <h2>Technical Questions</h2>

              {result.result.technical_questions.map((q, index) => (
                <div
                  key={index}
                  style={{
                    border: "1px solid #ddd",
                    padding: "15px",
                    marginBottom: "10px",
                    borderRadius: "10px",
                  }}
                >
                  <strong>{q.question}</strong>
                  <p>Difficulty: {q.difficulty}</p>
                </div>
              ))}

              <h2>Behavioral Questions</h2>

              {result.result.behavioral_questions?.map((q, index) => (
                <div
                  key={index}
                  style={{
                    border: "1px solid #ddd",
                    padding: "15px",
                    marginBottom: "10px",
                    borderRadius: "10px",
                  }}
                >
                  <strong>{q.question}</strong>
                  <p>Difficulty: {q.difficulty}</p>
                </div>
              ))}
            </>
          )}
        </div>
      )}
    </div>
  );
}

export default ChatCopilot;