import React, { useState } from 'react';

export default function VideoList() {
  const [videos, setVideos] = useState([]);
  const [searchQuery, setSearchQuery] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const fetchVideos = async (query = '') => {
    setLoading(true);
    setError(null);
    try {
      const url = query
        ? `http://localhost:8000/api/videos/search/?q=${encodeURIComponent(query)}`
        : `http://localhost:8000/api/videos/`;
      const res = await fetch(url);
      if (!res.ok) throw new Error(`HTTP error! Status: ${res.status}`);
      const data = await res.json();
      setVideos(data);
    } catch (err) {
      setError('Failed to fetch videos. Please try again.');
      setVideos([]);
    } finally {
      setLoading(false);
    }
  };

  const handleSearch = (e) => {
    e.preventDefault();
    if (searchQuery.trim() === '') {
      setVideos([]);
      return;
    }
    fetchVideos(searchQuery.trim());
  };

  const handleClear = () => {
    setSearchQuery('');
    setVideos([]);
    setError(null);
  };

  return (
    <div className="container my-5">
      <h2 className="mb-4 text-primary text-center">YouTube Videos</h2>
      <form onSubmit={handleSearch} className="input-group mb-4">
        <input
          type="text"
          className="form-control"
          placeholder="Search videos..."
          value={searchQuery}
          onChange={(e) => setSearchQuery(e.target.value)}
        />
        <button type="submit" className="btn btn-primary">
          Search
        </button>
        <button
          type="button"
          className="btn btn-secondary"
          onClick={handleClear}
        >
          Clear
        </button>
      </form>

      {loading && (
        <div className="text-center text-muted">Loading...</div>
      )}

      {error && (
        <div className="alert alert-danger text-center">{error}</div>
      )}

      {!loading && !error && videos.length === 0 && (
        <p className="text-center text-muted">Enter a search query to start.</p>
      )}

      {!loading && !error && videos.length > 0 && (
        <div className="row">
          {videos.map((video) => (
            <div key={video.video_id} className="col-md-6 col-lg-4 mb-4">
              <div className="card h-100 shadow-sm">
                <img
                  src={video.thumbnail_url}
                  className="card-img-top"
                  alt={video.title}
                />
                <div className="card-body d-flex flex-column">
                  <h5 className="card-title">{video.title}</h5>
                  <p className="card-text text-truncate">{video.description}</p>
                  <p className="card-text mt-auto">
                    <small className="text-muted">
                      Published: {new Date(video.published_at).toLocaleString()}
                    </small>
                  </p>
                  <p className="card-text">
                    <small className="text-muted">Channel: {video.channel_title}</small>
                  </p>
                </div>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
