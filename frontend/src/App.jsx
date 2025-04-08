import React, { useState } from "react";
import axios from "axios";
import "./styles.css";

function App() {
  const [rfpFile, setRfpFile] = useState(null);
  const [companyFile, setCompanyFile] = useState(null);
  const [loading, setLoading] = useState(false);
  const [analysis, setAnalysis] = useState(null);
  const [error, setError] = useState("");

  const handleSubmit = async () => {
    if (!rfpFile || !companyFile) {
      setError("Please upload both files.");
      return;
    }

    setLoading(true);
    setError("");

    const formData = new FormData();
    formData.append("rfp_file", rfpFile);
    formData.append("company_file", companyFile);

    try {
      const res = await axios.post("http://127.0.0.1:8000/analyze/analyze/", formData, {
        headers: { "Content-Type": "multipart/form-data" },
      });
      setAnalysis(res.data); // no longer using res.data.analysis (direct keys now)
    } catch (err) {
      console.error(err);
      setError("Error analyzing files. Please try again.");
    }

    setLoading(false);
  };

  const renderAgentSummary = (result, label) => (
    <div className="summary-block">
      <h2>{label}</h2>
      {result?.summary ? <p>{result.summary}</p> : <p>No summary available.</p>}
    </div>
  );

  return (
    <div className="app-container">
      <h1 className="app-title">🚀 RFP Analyzer</h1>

      <div className="form-section">
        <label className="upload-label">
          📄 Upload RFP File:
          <input type="file" accept="application/pdf" onChange={(e) => setRfpFile(e.target.files[0])} />
        </label>

        <label className="upload-label">
          🏢 Upload Company Data:
          <input type="file" accept="application/pdf" onChange={(e) => setCompanyFile(e.target.files[0])} />
        </label>
      </div>

      <div className="button-wrapper">
        <button onClick={handleSubmit} className="analyze-button">
          {loading ? "Analyzing..." : "Analyze RFP"}
        </button>
      </div>

      {error && <div className="error-text">{error}</div>}

      <div className="summary-container">
        {analysis && (
          <>
            {renderAgentSummary(analysis.compliance, "✅ Compliance")}
            {renderAgentSummary(analysis.eligibility, "🧾 Eligibility")}
            {renderAgentSummary(analysis.risk, "⚠️ Risk")}
            {renderAgentSummary(analysis.checklist, "📋 Submission Checklist")}
          </>
        )}
      </div>
    </div>
  );
}

export default App;
