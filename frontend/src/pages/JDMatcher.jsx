import { useState } from "react";
import api from "../services/api";

function JDMatcher() {
  const [resumeText, setResumeText] = useState("");
  const [jobDescription, setJobDescription] = useState("");

  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const matchResume = async () => {
    try {
      setLoading(true);

      const response = await api.post(
        "/jd-match",
        {
          resume_text: resumeText,
          job_description: jobDescription
        }
      );

      setResult(response.data);
    } catch (error) {
      console.error(error);
      alert("JD Match Failed");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <h1>JD Matcher</h1>

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

      <h3>Job Description</h3>

      <textarea
        rows="10"
        cols="100"
        value={jobDescription}
        onChange={(e) => setJobDescription(e.target.value)}
        placeholder="Paste Job Description..."
      />

      <br />
      <br />

      <button onClick={matchResume}>
        Match Resume
      </button>

      {loading && <p>Matching...</p>}

      {result && (
        <div style={{ marginTop: "30px" }}>
          <h2>
            Match Score: {result.match_score}%
          </h2>

          <h3>Matching Skills</h3>

          <ul>
            {result.matching_skills?.map(
              (skill, index) => (
                <li key={index}>{skill}</li>
              )
            )}
          </ul>

          <h3>Missing Skills</h3>

          <ul>
            {result.missing_skills?.map(
              (skill, index) => (
                <li key={index}>{skill}</li>
              )
            )}
          </ul>

          <h3>Recommendations</h3>

          <ul>
            {result.recommendations?.map(
              (item, index) => (
                <li key={index}>{item}</li>
              )
            )}
          </ul>
        </div>
      )}
    </div>
  );
}

export default JDMatcher;