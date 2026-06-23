import { useState } from "react";
import api from "../services/api";

function ResumeAnalyzer() {
  const [resumeText, setResumeText] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const analyzeResume = async () => {
    try {
      setLoading(true);

      const response = await api.post(
        "/resume-analysis",
        {
          resume_text: resumeText
        }
      );

      setResult(response.data);
    } catch (error) {
      console.error(error);
      alert("Resume analysis failed");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <h1>Resume Analyzer</h1>

      <textarea
        rows="15"
        cols="100"
        placeholder="Paste Resume Here..."
        value={resumeText}
        onChange={(e) => setResumeText(e.target.value)}
      />

      <br />
      <br />

      <button onClick={analyzeResume}>
        Analyze Resume
      </button>

      {loading && <p>Analyzing...</p>}

      {result && (
        <div style={{ marginTop: "30px" }}>
          <h2>Summary</h2>
          <p>{result.summary}</p>

          <h2>Skills</h2>
          <ul>
            {result.skills?.map((skill, index) => (
              <li key={index}>{skill}</li>
            ))}
          </ul>

          <h2>Strengths</h2>
          <ul>
            {result.strengths?.map((item, index) => (
              <li key={index}>{item}</li>
            ))}
          </ul>

          <h2>Missing Skills</h2>
          <ul>
            {result.missing_skills?.map((item, index) => (
              <li key={index}>{item}</li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default ResumeAnalyzer;