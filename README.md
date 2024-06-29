## Running Docker (w/ Flask) examples

- Navigate into one of the respective folders inside of `docker`.
- Make sure the Docker daemon is running (i.e. have Docker Desktop running).
- Run `docker build`: `docker build -t <name_of_image>:<tag_name> .` (You can use 'latest' as the tag name'.)
- Start a Docker container of the new image: `docker run -p 5001:5001 --rm <name_of_image>:<tag_name>`.
- Open `localhost:5001` in your browser to see the Flask app.
