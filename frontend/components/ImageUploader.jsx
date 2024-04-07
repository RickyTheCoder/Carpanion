import React, { useState } from 'react';

const ImageUploader = () => {
  const [selectedImage, setSelectedImage] = useState(null);

  const handleImageChange = (e) => {
    setSelectedImage(e.target.files[0]);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!selectedImage) {
      console.error('No image selected');
      return;
    }

    const reader = new FileReader();
    reader.onloadend = () => {
      const base64ImageContent = reader.result.replace(/^data:image\/(png|jpg|jpeg);base64,/, '');
      fetch('/api/image-to-text/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          // Make sure to get the CSRF token as needed
        },
        body: JSON.stringify({ image: base64ImageContent })
      })
      .then(response => response.json())
      .then(data => {
        console.log('Success:', data);
        // Handle success
      })
      .catch((error) => {
        console.error('Error:', error);
        // Handle errors here
      });
    };
    reader.readAsDataURL(selectedImage);
  };

  return (
    <form onSubmit={handleSubmit}>
      <input 
        type="file" 
        accept="image/*" 
        onChange={handleImageChange} 
      />
      <button type="submit">Upload</button>
    </form>
  );
};

export default ImageUploader;
