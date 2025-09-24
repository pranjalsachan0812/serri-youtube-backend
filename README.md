# YouTube Video Search App

This is a full-stack web application that allows users to search for recent YouTube videos by keyword. The backend is built with Django and the frontend is developed using React with Bootstrap for styling.

---

## Features

- Search YouTube videos by keyword query (currently focused on "cricket").
- Fetches latest videos from YouTube's Data API and stores them in a local database.
- Provides a paginated, card-based UI with video details including title, description, publish date, thumbnail, and channel.
- Displays loading and error states in the UI.
- Backend API built with Django REST Framework.
- Frontend developed with React and Bootstrap CSS for responsive design.

---

## Prerequisites

- Python 3.10+ and Node.js installed.
- Django and React dependencies installed.
- A valid YouTube Data API v3 key.

---

## Setup Instructions

### Backend

1. Clone the repository and navigate to the backend directory.
2. Create and activate a Python virtual environment.
3. Install dependencies:

pip install -r requirements.txt


4. Create a `.env` file in the backend folder and add your YouTube API key:

YOUTUBE_API_KEY=YOUR_YOUTUBE_API_KEY_HERE


5. Apply Django migrations:

python manage.py migrate

6. Run the fetch script to populate the database with cricket-related videos:

python manage.py shell

Then in the shell:

from videos.youtube_fetcher import fetch_latest_videos
fetch_latest_videos()

Note: The app is currently set up to fetch videos related to the keyword **"cricket"**.

7. Start the Django development server:

python manage.py runserver 8000

### Frontend

1. Navigate to the frontend React app directory.
2. Install dependencies:

npm install

3. Start the React development server:

npm start

4. Open [http://localhost:3000](http://localhost:3000) in your browser.

---

## Usage

- Enter your video search terms in the frontend search box. The backend currently supports searching the videos stored in the database, which are primarily cricket-related videos fetched from YouTube.
- Results will be displayed as video cards with thumbnails and details.
- Use the **Clear** button to reset the search.

---

## Notes

- The backend fetch function filters videos published **after the latest video stored** or a default past date.
- YouTube API usage is subject to quota limits; fetching large historical data may require pagination or batch fetching.
- The search is limited to videos related to **"cricket"** as per the current backend fetch setup.
- CORS is enabled for local development to allow frontend-backend communication.

---

## Future Improvements

- Make search query dynamic for fetching videos beyond "cricket".
- Implement pagination in frontend and backend.
- Add authentication and user personalization.
- Deploy the app using production-grade servers and configurations.

---

## License

This project is licensed under the MIT License.