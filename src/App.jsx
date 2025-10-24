import React, { useState } from 'react';
import './App.css';

const peRatioData = {
  indices: [
    { name: "標普500", pe: 28.5, avg: 16.8, status: "高估" },
    { name: "道瓊工業", pe: 26.8, avg: 15.2, status: "高估" },
    { name: "納斯達克", pe: 35.2, avg: 22.4, status: "高估" },
    { name: "恒生指數", pe: 9.2, avg: 12.8, status: "低估" }
  ]
};

function App() {
  const [tab, setTab] = useState('overview');

  return (
    <div style={{ minHeight: '100vh', padding: '20px', backgroundColor: '#f5f5f5' }}>
      <div style={{ maxWidth: '1200px', margin: '0 auto' }}>
        <h1 style={{ textAlign: 'center', color: '#333', marginBottom: '30px' }}>
          歷史本益比分析報告
        </h1>

        <div style={{ marginBottom: '20px', borderBottom: '2px solid #ddd' }}>
          <button 
            onClick={() => setTab('overview')}
            style={{ 
              padding: '10px 20px', 
              marginRight: '10px',
              backgroundColor: tab === 'overview' ? '#007bff' : '#f0f0f0',
              color: tab === 'overview' ? 'white' : '#333',
              border: 'none',
              cursor: 'pointer',
              borderRadius: '4px'
            }}
          >
            總覽
          </button>
          <button 
            onClick={() => setTab('sentiment')}
            style={{ 
              padding: '10px 20px',
              backgroundColor: tab === 'sentiment' ? '#007bff' : '#f0f0f0',
              color: tab === 'sentiment' ? 'white' : '#333',
              border: 'none',
              cursor: 'pointer',
              borderRadius: '4px'
            }}
          >
            市場情緒
          </button>
        </div>

        {tab === 'overview' && (
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(250px, 1fr))', gap: '20px' }}>
            {peRatioData.indices.map((index) => (
              <div key={index.name} style={{ 
                backgroundColor: 'white', 
                padding: '20px', 
                borderRadius: '8px',
                boxShadow: '0 2px 4px rgba(0,0,0,0.1)'
              }}>
                <h3 style={{ margin: '0 0 15px 0', color: '#333' }}>{index.name}</h3>
                <div style={{ marginBottom: '10px' }}>
                  <span style={{ color: '#666' }}>歷史平均：</span>
                  <span style={{ fontWeight: 'bold' }}>{index.avg}</span>
                </div>
                <div style={{ marginBottom: '10px' }}>
                  <span style={{ color: '#666' }}>當前水平：</span>
                  <span style={{ fontWeight: 'bold', fontSize: '18px' }}>{index.pe}</span>
                </div>
                <div>
                  <span style={{ color: '#666' }}>狀態：</span>
                  <span style={{ 
                    fontWeight: 'bold',
                    color: index.status === '高估' ? '#dc3545' : '#28a745',
                    marginLeft: '5px'
                  }}>
                    {index.status}
                  </span>
                </div>
              </div>
            ))}
          </div>
        )}

        {tab === 'sentiment' && (
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))', gap: '20px' }}>
            <div style={{ 
              backgroundColor: 'white', 
              padding: '30px', 
              borderRadius: '8px',
              boxShadow: '0 2px 4px rgba(0,0,0,0.1)',
              textAlign: 'center'
            }}>
              <h3 style={{ marginTop: 0 }}>美國市場恐懼與貪婪指數</h3>
              <div style={{ fontSize: '48px', fontWeight: 'bold', color: '#f97316', margin: '20px 0' }}>
                29
              </div>
              <p style={{ color: '#666' }}>恐懼</p>
              <p style={{ color: '#999', fontSize: '14px' }}>美國市場當前處於恐懼狀態</p>
            </div>
            <div style={{ 
              backgroundColor: 'white', 
              padding: '30px', 
              borderRadius: '8px',
              boxShadow: '0 2px 4px rgba(0,0,0,0.1)',
              textAlign: 'center'
            }}>
              <h3 style={{ marginTop: 0 }}>香港市場恐懼與貪婪指數</h3>
              <div style={{ fontSize: '48px', fontWeight: 'bold', color: '#22c55e', margin: '20px 0' }}>
                67
              </div>
              <p style={{ color: '#666' }}>貪婪</p>
              <p style={{ color: '#999', fontSize: '14px' }}>香港市場當前處於貪婪狀態</p>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;

