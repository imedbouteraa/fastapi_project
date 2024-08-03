
# OCR API with FastAPI

This project is an OCR (Optical Character Recognition) API built with FastAPI. It processes images of driver's licenses,carte crise,french id card, extracting key information such as the holder's name, date of birth, license number, and more. The API can be integrated with mobile apps or other services.

## Features

- **Driver's License OCR**: Extract information from images of driver's licenses.
- **Custom Image OCR**: Process custom images to extract text data.
- **FastAPI**: Leverages FastAPI for high performance and ease of use.
- **Deployed on Heroku**: Easily deployable on Heroku or other cloud services.

## Project Structure


ocr_fastapi/
├── main.py
├── serializers.py
├── views.py
├── Procfile
├── requirements.txt
├── runtime.txt (optional)
└── media/


## Getting Started

### Prerequisites

- Python 3.8+
- Git
- Heroku CLI (for deployment)

### Installation

1. **Clone the repository**:

   git clone https://github.com/imedbouteraa/fastapi_project.git
   cd your-repo-name
   

2. **Create a virtual environment**:


   python -m venv venv
   

3. **Activate the virtual environment**:

   - On Windows:

  
     venv\Scripts\activate
     

   - On macOS/Linux:

    
     source venv/bin/activate
    

4. **Install the dependencies**:

   pip install -r requirements.txt
   

### Running the Application

1. **Start the FastAPI server**:

   
   uvicorn main:app --reload
   

2. **Access the API documentation**:

   Open your web browser and go to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to see the interactive API documentation provided by Swagger UI.

### API Endpoints

- **GET /**: Welcome message.
- **POST /api/ocr/driver_license/**: Upload an image of a driver's license to extract information.
- **POST /api/ocr/custom/**: Upload a custom image to extract text data.

### Example Request

**Endpoint**: `/api/ocr/driver_license/`

**Method**: `POST`

**Body**: `form-data`

- Key: `image`
- Type: `File`
- Value: Select an image file of a driver's license

### Deployment

To deploy this application on Heroku, follow these steps:

1. **Create a `Procfile`**:

  
   echo "web: uvicorn main:app --host 0.0.0.0 --port \$PORT" > Procfile
   

2. **Create a `requirements.txt`**:

  
   pip freeze > requirements.txt
   

3. **Create a `runtime.txt` (Optional)**:

  
   echo "python-3.8.12" > runtime.txt
 

4. **Initialize Git**:

   
   git init
   git add .
   git commit -m "Initial commit"
  

5. **Create a Heroku App**:

  
   heroku create your-app-name
 

6. **Deploy to Heroku**:

  
   git push heroku main
   

7. **Open Your App**:

  
   heroku open
  

### Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.




Happy coding!


