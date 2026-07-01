import { Link, useLocation } from "react-router-dom";

function Sidebar() {
const location = useLocation();

const menuItem = (path, label, icon) => ({
display: "block",
padding: "12px 15px",
marginBottom: "8px",
borderRadius: "10px",
textDecoration: "none",
color: "white",
background:
location.pathname === path
? "#374151"
: "transparent"
});

return (
<div
style={{
width: "260px",
background: "#111827",
color: "white",
minHeight: "100vh",
padding: "25px",
boxSizing: "border-box"
}}
>
<h2
style={{
marginBottom: "30px"
}}
>
🤖 AI Career Copilot </h2>

```
  <Link
    to="/"
    style={menuItem("/", "Dashboard")}
  >
    📊 Dashboard
  </Link>

  <Link
    to="/resume"
    style={menuItem("/resume")}
  >
    📄 Resume Analyzer
  </Link>

  <Link
    to="/jd"
    style={menuItem("/jd")}
  >
    🎯 JD Matcher
  </Link>

  <Link
    to="/interview"
    style={menuItem("/interview")}
  >
    💼 Interview Prep
  </Link>

  <Link
    to="/career"
    style={menuItem("/career")}
  >
    🚀 Career Advisor
  </Link>

  <Link
    to="/copilot"
    style={menuItem("/copilot")}
  >
    🤖 AI Copilot
  </Link>

  <div
    style={{
      position: "absolute",
      bottom: "20px",
      left: "25px",
      color: "#9CA3AF",
      fontSize: "14px"
    }}
  >
    Powered by LangGraph + FAISS
  </div>
</div>

);
}

export default Sidebar;
