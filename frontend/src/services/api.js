import axios from "axios";

const api = axios.create({
  baseURL:
    "https://agentic-ai-career-copilot-platform.onrender.com"
});

export default api;