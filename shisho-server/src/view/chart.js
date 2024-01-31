import React from 'react';
import axios from 'axios';

import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
} from 'chart.js';

import { Line } from 'react-chartjs-2';

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
);

export default function App() {
  const [data, setData] = React.useState([]);

  React.useEffect(() => {
    axios.get('http://127.0.0.1:5000/history').then((response) => {
      const data = response.data;

      setData({
        labels: data.map((record) => record[0]),
              datasets: [
                {
                  label: 'ETH',
                  data: data.map((record) => record[1]),
                  backgroundColor: 'rgba(255, 99, 132, 0.2)',
                  borderColor: 'rgba(255, 99, 132, 1)',
                }
              ]
            });
          });
  }, []);

  if (data.length === 0) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <Line data={data}></Line>
    </div>
  );
}