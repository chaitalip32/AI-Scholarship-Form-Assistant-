import { useState, useEffect } from "react";
import axios from "axios";

function App() {
  const [message, setMessage] = useState("Loading...");

  useEffect(() => {
    axios
      .get("http://localhost:8000/")
      .then((response) => {
        console.log(response.data);
        setMessage(response.data.message);
      })
      .catch((error) => {
        console.error("API Error:", error);
        setMessage("Failed to connect backend");
      });
  }, []);

  return (
    <div>
      <h1>{message}</h1>
    </div>
  );
}

export default App;