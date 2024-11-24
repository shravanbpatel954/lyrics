from flask import Flask, request, jsonify
from g4f.client import Client

app = Flask(__name__)

# Route for generating lyrics
@app.route("/generate-lyrics", methods=["POST"])
def generate_lyrics():
    # Get the request data
    data = request.get_json()
    prompt = data.get("prompt")
    language = data.get("language")
    song_style = data.get("songStyle")

    # Ensure all required fields are provided
    if not prompt or not language or not song_style:
        return jsonify({"error": "Please provide all required fields."}), 400

    try:
        # Construct the text prompt for the GPT model
        text_prompt = (
    f"Compose a {song_style} song in {language} based on the following prompt: \"{prompt}\". "
    f"Include a clear title, verses, and chorus. Do not write any intro or conclusion lines. "
    f"Ensure the song has a proper structure ."
                    )

        # Initialize the g4f client
        client = Client()

        # Generate lyrics using the GPT model
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # Change the model if needed
            messages=[{"role": "user", "content": text_prompt}],
        )

        # Extract the generated lyrics from the response
        lyrics = response.choices[0].message.content.strip()

        # Send the generated lyrics back as a response
        return jsonify({"lyrics": lyrics})

    except Exception as e:
        print(f"Error generating lyrics: {e}")
        return jsonify({"error": "Failed to generate lyrics."}), 500


# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True, port=5001)
