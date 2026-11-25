import { useState } from "react";
import { checkBackendHealth } from "./services/api";

function App() {

    const [data, setData] = useState(null);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);

    const handleCheckConnection = async () => {

        setLoading(true);
        setError(null);
        setData(null);

        try {

            const result = await checkBackendHealth();
            setData(result);

        } catch (err) {

            setError(err.message);

        } finally {

            setLoading(false);

        }
    };

    return (
        <main style={{ padding: "40px" }}>

            <h1>AutoMind LK</h1>

            <p>Frontend and Backend Integration Test</p>

            <button
                onClick={handleCheckConnection}
                disabled={loading}
            >
                {loading
                    ? "Connecting..."
                    : "Check Backend Connection"}
            </button>

            {data && (
                <div style={{ color: "green" }}>
                    <h3>Backend Connected Successfully</h3>
                    <p>Status: {data.status}</p>
                    <p>Service: {data.service}</p>
                </div>
            )}

            {error && (
                <div style={{ color: "red" }}>
                    <h3>Connection Failed</h3>
                    <p>{error}</p>
                </div>
            )}

        </main>
    );
}

export default App;