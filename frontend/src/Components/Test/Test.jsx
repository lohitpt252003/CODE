import React, { useState, useEffect } from "react";
import Skeleton from "react-loading-skeleton";
import "react-loading-skeleton/dist/skeleton.css";

// Full Page Skeleton Loader component
const FullPageLoader = () => {
    return (
        <div
            style={{
                display: "flex",
                justifyContent: "center",
                alignItems: "center",
                height: "100vh",
                backgroundColor: "#f0f0f0",
                flexDirection: "column",
            }}
        >
            <Skeleton circle={true} height={100} width={100} />
            <Skeleton width={200} />
            <Skeleton width={300} />
            <Skeleton count={5} width={600} />
        </div>
    );
};

const App = () => {
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        // Simulate loading data (replace with actual API calls or data fetching)
        setTimeout(() => setLoading(false), 3000); // Simulated 3 seconds loading
    }, []);

    return (
        <div style={{ minHeight: "100vh" }}>
            {loading ? (
                <FullPageLoader />
            ) : (
                <div style={{ padding: "20px" }}>
                    {/* Your actual page content goes here */}
                    <h1>Welcome to My Website</h1>
                    <p>This is the real content of your page!</p>
                    <p>All skeleton loaders are hidden once the content is ready.</p>
                </div>
            )}
        </div>
    );
};

export default App;
