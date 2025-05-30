import React, { useEffect, useState } from 'react';
import { fetchHealthData } from '../api/healthinfoApi';
import { HealthData } from '../types';

const HealthDataList: React.FC = () => {
    const [healthData, setHealthData] = useState<HealthData[]>([]);
    const [loading, setLoading] = useState<boolean>(false);
    const [patientId, setPatientId] = useState<string>('1'); // Default patient ID

    const loadHealthData = async () => {
        setLoading(true);
        try {
            const data = await fetchHealthData(patientId);
            setHealthData([data]); // Adjust based on API response structure
        } catch (error) {
            console.error('Error fetching health data:', error);
        } finally {
            setLoading(false);
        }
    };

    useEffect(() => {
        loadHealthData();
    }, [patientId]);

    return (
        <div className="container">
            <h2>Health Data</h2>
            <input
                type="text"
                value={patientId}
                onChange={(e) => setPatientId(e.target.value)}
                placeholder="Enter Patient ID"
            />
            <button onClick={loadHealthData}>Fetch Data</button>
            {loading ? (
                <p>Loading health data...</p>
            ) : (
                healthData.map((data) => (
                    <div key={data.id} className="card">
                        <h3 className="card-title">{data.name}</h3>
                        <p className="card-content">Age: {data.age}</p>
                        <p className="card-content">Medical History: {data.medicalHistory.join(', ')}</p>
                    </div>
                ))
            )}
        </div>
    );
};

export default HealthDataList;