import { useEffect, useState } from 'react';
import api from '../services/api';

const Dashboard = () => {
  const [patientData, setPatientData] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const data = await api.getPatientInfo();
        setPatientData(data);
      } catch (error) {
        console.error('Error fetching patient data:', error);
      }
    };
    fetchData();
  }, []);

  return (
    <div>
      {patientData && (
        <div className="patient-info">
          <h2>{patientData.name[0].text}</h2>
          <p>Gender: {patientData.gender}</p>
          <p>DOB: {patientData.birthDate}</p>
        </div>
      )}
    </div>
  );
};