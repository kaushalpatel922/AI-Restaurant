import React, { useState } from "react";
import axios from "axios";

const uploadImage = () => {
  const [image, setImage] = useState(null);

  const handleImageChange = () => {
    setImage(e.target.files[0]);
  };

  return (
    <div className="upload-container">
      <h1>Upload Image here..</h1>
      <input type="file" onChange={handleImageChange} />
    </div>
  );
};

export default uploadImage;
