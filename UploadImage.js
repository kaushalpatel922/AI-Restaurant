import React, { useState } from "react";
import axios from "axios";

const uploadImage = () => {
  const [image, setImage] = useState(null);

  const handleImageChange = () => {
    setImage(e.target.files[0]);
  };

  const handleUpload = async () => {
    if(!image) {
      alert("Please upload an image!")
      return;
    }

    const formData = new FormData();
    formData.append("file", image);

    try {
      const response = await axios.post("http://127.0.0.1:5000/analyze", formData);
    } catch(error) {
      alert("Error processing image!")
    }
  }

  return (
    <div className="upload-container">
      <h1>Upload Image here..</h1>
      <input type="file" onChange={handleImageChange} />
      <button onClick={handleUpload}>Analyze</button>
    </div>
  );
};

export default uploadImage;
