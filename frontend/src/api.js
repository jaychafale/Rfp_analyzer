// src/api.js
import axios from 'axios';

const API_BASE = 'http://127.0.0.1:8000/analyze/analyze/';

export async function uploadAndAnalyze(rfpFile, companyFile) {
  const formData = new FormData();
  formData.append('rfp_file', rfpFile);
  formData.append('company_file', companyFile);

  try {
    const response = await axios.post(API_BASE, formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    });
    return response.data;
  } catch (err) {
    console.error(err);
    return { error: err?.response?.data?.error || 'Unknown error' };
  }
}
