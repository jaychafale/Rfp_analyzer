// src/components/ResultViewer.jsx
import React from 'react';

export default function ResultViewer({ data }) {
  if (!data) return null;
  if (data.error) return <div className="error">❌ {data.error}</div>;

  return (
    <div className="results">
      <h3>✅ Analysis Result</h3>
      {data.analysis.map((item, idx) => (
        <div className="chunk-result" key={idx}>
          <h4>📌 Chunk {idx + 1}</h4>
          <pre>{JSON.stringify(item, null, 2)}</pre>
        </div>
      ))}
    </div>
  );
}
