import { useState } from "react";
import api from "../services/api";

function CareerAdvisor() {
  const [question, setQuestion] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const askQuestion = async () => {
    try {
      setLoading(true);
      setResult(null);

      const response = await api.post("/career-advice", {
        question,
      });

      console.log("Career Advice Response:", response.data);

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

  return (
    <div>
      <h1>🚀 Career Advisor</h1>

      <textarea
        rows={6}
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        placeholder="Ask a career question..."
        style={{
          width: "100%",
          padding: "12px",
          borderRadius: "8px",
          marginBottom: "15px",
        }}
      />

      <button onClick={askQuestion} disabled={loading}>
        Ask
      </button>

      {loading && (
        <p style={{ marginTop: "20px" }}>
          🤖 Thinking...
        </p>
      )}

      {!loading && !result && (
        <p style={{ marginTop: "20px", color: "gray" }}>
          Ask a question to get career guidance.
        </p>
      )}

      {result?.answer && (
        <div
          style={{
            marginTop: "30px",
            background: "white",
            padding: "20px",
            borderRadius: "12px",
            boxShadow: "0 2px 10px rgba(0,0,0,0.1)",
          }}
        >
          <h2>Answer</h2>

          <div
            style={{
              whiteSpace: "pre-wrap",
              lineHeight: "1.8",
            }}
          >
            {typeof result.answer === "string"
              ? result.answer
              : result.answer?.content}
          </div>

          {result.sources?.length > 0 && (
            <>
              <h3 style={{ marginTop: "20px" }}>
                Sources
              </h3>

              <div style={{ display: "flex", flexWrap: "wrap", gap: "10px" }}>
                {result.sources.map((source, index) => (
                  <span
                    key={index}
                    style={{
                      background: "#dbeafe",
                      color: "#1d4ed8",
                      padding: "6px 12px",
                      borderRadius: "20px",
                      fontSize: "12px",
                    }}
                  >
                    {source}
                  </span>
                ))}
              </div>
            </>
          )}
        </div>
      )}
    </div>
  );
}

export default CareerAdvisor;