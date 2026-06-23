import { BrowserRouter, Routes, Route } from "react-router-dom";
import Chat from "./pages/Chat";
import Sidebar from "./components/Sidebar";
import ChatCopilot from "./pages/ChatCopilot";
import Dashboard from "./pages/Dashboard";
import ResumeAnalyzer from "./pages/ResumeAnalyzer";
import JDMatcher from "./pages/JDMatcher";
import InterviewPrep from "./pages/InterviewPrep";
import CareerAdvisor from "./pages/CareerAdvisor";

function App() {
  return (
    <BrowserRouter>
      <div style={{ display: "flex" }}>
        <Sidebar />

        <div
          style={{
            flex: 1,
            padding: "30px"
          }}
        >
          <Routes>
            <Route path="/" element={<Dashboard />} />
            <Route path="/resume" element={<ResumeAnalyzer />} />
            <Route path="/jd" element={<JDMatcher />} />
            <Route path="/interview" element={<InterviewPrep />} />
            <Route path="/career" element={<CareerAdvisor />} />
            <Route path="/chat" element={<Chat />} />
            <Route path="/copilot" element={<ChatCopilot />} />
          </Routes>
        </div>
      </div>
    </BrowserRouter>
  );
}

export default App;