import axios from 'axios';

const API_BASE_URL = 'http://127.0.0.1:8000/api'

export interface HealthData {
    id: string;
    name: string;
    age: number;
    medicalHistory: string[];
}

export interface HealthRecord {
    recordId: string;
    patientId: string;
    details: string;
    date: string;
}

export const fetchHealthData = async (patientId: string): Promise<HealthData> => {
    const response = await axios.get<HealthData>(`${API_BASE_URL}/healthdata/${patientId}`);
    return response.data;
};

export const updateHealthRecord = async (recordId: string, updatedData: Partial<HealthRecord>): Promise<HealthRecord> => {
    const response = await axios.put<HealthRecord>(`${API_BASE_URL}/healthrecords/${recordId}`, updatedData);
    return response.data;
};