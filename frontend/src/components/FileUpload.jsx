// src/components/FileUpload.jsx
import React, { useState } from 'react';
import { uploadAndAnalyze } from '../api';

export default function FileUpload({ onResult }) {
  const [rfp, setRfp] = useState(null);
  const [company, setCompany] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleUpload = async () => {
    if (!rfp || !company) return alert('Both files are required!');
    setLoading(true);
    const result = await uploadAndAnalyze(rfp, company);
    setLoading(false);
    onResult(result);
  };

  return (
    <div className="upload-box">
      <h2>📄 RFP Analyzer</h2>
      <input type="file" onChange={(e) => setRfp(e.target.files[0])} />
      <input type="file" onChange={(e) => setCompany(e.target.files[0])} />
      <button onClick={handleUpload} disabled={loading}>
        {loading ? 'Analyzing...' : 'Upload & Analyze'}
      </button>
    </div>
  );
}
