const axios = require("axios");  // Import axios for making HTTP requests

// Lyrics generation function that calls the Python server
exports.generateLyrics = async (req, res) => {
  const { prompt, language, songStyle } = req.body;

  // Ensure all required fields are provided
  if (!prompt || !language || !songStyle) {
    return res.status(400).json({ error: "Please provide all required fields." });
  }

  try {
    // Construct the request payload to send to the Python server
    const requestPayload = {
      prompt: prompt,
      language: language,
      songStyle: songStyle,
    };

    // Make the request to the Python server's /generate-lyrics endpoint
    const pythonServerResponse = await axios.post("http://localhost:5001/generate-lyrics", requestPayload);

    // Extract the generated lyrics from the Python server's response
    const lyrics = pythonServerResponse.data.lyrics;

    // Send the generated lyrics back to the client
    res.status(200).json({ lyrics });
  } catch (error) {
    console.error("Error generating lyrics:", error.message);
    res.status(500).json({ error: "Failed to generate lyrics." });
  }
};
