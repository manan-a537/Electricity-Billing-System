const API_BASE_URL = 'http://localhost:5000/api';

export const apiService = {
    async getReadings() {
        const response = await fetch(`${API_BASE_URL}/readings`);
        return response.json();
    },

    async getBill(year, month) {
        const response = await fetch(`${API_BASE_URL}/bills/${year}/${month}`);
        return response.json();
    },

    async getConsumptionHistory(months = 6) {
        const response = await fetch(`${API_BASE_URL}/consumption/history?months=${months}`);
        return response.json();
    },

    async getAlerts() {
        const response = await fetch(`${API_BASE_URL}/alerts`);
        return response.json();
    },

    async addReading(reading) {
        const response = await fetch(`${API_BASE_URL}/readings`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(reading),
        });
        return response.json();
    },
};