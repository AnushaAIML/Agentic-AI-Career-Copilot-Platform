import { useState } from "react";
import api from "../services/api";

function Chat() {
  const [message, setMessage] = useState("");
  const [response, setResponse] = useState(null);
  const [loading, setLoading] = useState(false);

  const sendMessage = async () => {
    try {
      setLoading(true);

      const res = await api.post(
        "/chat",
        {
          user_input: message,
          resume_text: "",
          job_description: "",
          target_role: ""
        }
      );

      setResponse(res.data);
    } catch (error) {
      console.error(error);
      alert("Chat failed");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <h1>AI Career Copilot</h1>

      <textarea
        rows="5"
        cols="100"
        placeholder="Ask anything..."
        value={message}
        onChange={(e) => setMessage(e.target.value)}
      />

      <br />
      <br />

      <button onClick={sendMessage}>
        Send
      </button>

      {loading && <p>Thinking...</p>}

      {response && (
        <div style={{ marginTop: "30px" }}>
          <h2>Selected Tool</h2>

          <p>{response.selected_tool}</p>

          <h2>Result</h2>

          <pre>
            {JSON.stringify(
              response.result,
              null,
              2
            )}
          </pre>
        </div>
      )}
    </div>
  );
}

export default Chat;